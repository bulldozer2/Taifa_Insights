from django.contrib import admin
from .models import Sector, Indicator


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'sector', 'unit', 'frequency')
    list_filter = ('sector', 'frequency')
    search_fields = ('name', 'description')


from .models import Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')
