from django.db import models


class Sector(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Indicator(models.Model):
    FREQUENCY_CHOICES = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annual', 'Annual'),
    ]

    name = models.CharField(max_length=255)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='indicators')
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=50)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='monthly')

    class Meta:
        unique_together = ('name', 'sector')

    def __str__(self):
        return f"{self.name} ({self.sector.name})"


class Region(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=100, default='Kenya')

    def __str__(self):
        return f"{self.name}, {self.country}"
