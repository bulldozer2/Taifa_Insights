from rest_framework import viewsets
from apps.indicators.models import Sector, Indicator, Region
from apps.datasets.models import Dataset, DataPoint
from apps.insights.models import Insight
from .serializers import (
    SectorSerializer,
    IndicatorSerializer,
    DatasetSerializer,
    DataPointSerializer,
)


class SectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class IndicatorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Indicator.objects.select_related('sector').all()
    serializer_class = IndicatorSerializer


class DatasetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer


class DataPointViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataPoint.objects.select_related('indicator', 'region').all()
    serializer_class = DataPointSerializer
