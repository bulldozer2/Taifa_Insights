from django.shortcuts import render, get_object_or_404
from .models import Insight


def list_insights(request):
    insights = Insight.objects.filter(published=True)
    return render(request, 'insights/list.html', {'insights': insights})


def detail_insight(request, slug):
    insight = get_object_or_404(Insight, slug=slug, published=True)
    return render(request, 'insights/detail.html', {'insight': insight})
