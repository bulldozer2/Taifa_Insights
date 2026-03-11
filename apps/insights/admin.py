from django.contrib import admin
from .models import Insight


@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'created_at')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'summary', 'content')
