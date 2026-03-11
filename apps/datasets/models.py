from django.db import models
from apps.indicators.models import Indicator
from apps.indicators.models import Region


class Dataset(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class DataPoint(models.Model):
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE, related_name='datapoints')
    region = models.ForeignKey('apps.indicators.Region', on_delete=models.CASCADE, related_name='datapoints')
    date = models.DateField()
    year = models.PositiveSmallIntegerField()
    month = models.PositiveSmallIntegerField(null=True, blank=True)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    source = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('indicator', 'region', 'date')
        ordering = ['date']

    def __str__(self):
        return f"{self.indicator.name} - {self.region.name} @ {self.date}"
