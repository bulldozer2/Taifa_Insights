from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from apps.indicators.models import Indicator
from apps.datasets.models import DataPoint


def dashboards_home(request):
    slugs = ['tourism', 'transport', 'manufacturing']
    return render(request, 'dashboards/index.html', {'categories': slugs})


def indicator_dashboard(request, slug):
    indicator = get_object_or_404(Indicator, name__icontains=slug)
    return render(request, 'dashboards/indicator_dashboard.html', {'indicator': indicator})


def indicator_datapoints_api(request, slug):
    indicator = get_object_or_404(Indicator, name__icontains=slug)
    datapoints = DataPoint.objects.filter(indicator=indicator).order_by('date')
    data = {
        'labels': [dp.date.strftime('%Y-%m-%d') for dp in datapoints],
        'values': [float(dp.value) for dp in datapoints],
    }
    return JsonResponse(data)
