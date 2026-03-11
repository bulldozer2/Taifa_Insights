import csv
import os
from django.core.management.base import BaseCommand, CommandError
from apps.datasets.models import DataPoint
from apps.indicators.models import Indicator, Region
from django.db import transaction
from datetime import datetime


class Command(BaseCommand):
    help = 'Import data points from a CSV file into DataPoint table'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_path = options['csv_file']
        if not os.path.exists(csv_path):
            raise CommandError(f"CSV file not found: {csv_path}")

        created_count = 0
        updated_count = 0

        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            required_columns = ['indicator', 'region', 'date', 'value', 'source']

            for col in required_columns:
                if col not in reader.fieldnames:
                    raise CommandError(f"Missing required column: {col}")

            with transaction.atomic():
                for row in reader:
                    indicator_name = row['indicator'].strip()
                    region_name = row['region'].strip()
                    source = row.get('source', '').strip()
                    date_str = row['date'].strip()
                    value_str = row['value'].strip()

                    if not indicator_name or not region_name or not date_str or not value_str:
                        self.stdout.write(self.style.WARNING(f"Skipping invalid row: {row}"))
                        continue

                    try:
                        date = datetime.fromisoformat(date_str).date()
                    except ValueError:
                        self.stdout.write(self.style.WARNING(f"Invalid date format for row: {row}"))
                        continue

                    try:
                        value = float(value_str)
                    except ValueError:
                        self.stdout.write(self.style.WARNING(f"Invalid numeric value for row: {row}"))
                        continue

                    from apps.indicators.models import Sector
                    default_sector, _ = Sector.objects.get_or_create(name='Unspecified', defaults={'description': 'Automatically created sector for import.'})

                    indicator, _ = Indicator.objects.get_or_create(
                        name=indicator_name,
                        defaults={'description': '', 'unit': '', 'frequency': 'monthly', 'sector': default_sector}
                    )
                    region, _ = Region.objects.get_or_create(name=region_name, defaults={'country': 'Kenya'})

                    datapoint, created = DataPoint.objects.update_or_create(
                        indicator=indicator,
                        region=region,
                        date=date,
                        defaults={
                            'year': date.year,
                            'month': date.month,
                            'value': value,
                            'source': source,
                        }
                    )

                    if created:
                        created_count += 1
                    else:
                        updated_count += 1

        self.stdout.write(self.style.SUCCESS(f"Import complete: {created_count} rows created, {updated_count} rows updated."))
