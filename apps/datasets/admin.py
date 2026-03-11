from django.contrib import admin
from .models import Dataset, DataPoint


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'created_at')
    search_fields = ('name', 'description', 'source')


@admin.register(DataPoint)
class DataPointAdmin(admin.ModelAdmin):
    list_display = ('indicator', 'region', 'date', 'value', 'source')
    list_filter = ('indicator', 'region', 'source')
    search_fields = ('indicator__name', 'region__name', 'source')
