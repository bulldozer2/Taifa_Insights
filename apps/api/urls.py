from django.urls import path, include
from rest_framework import routers
from .views import SectorViewSet, IndicatorViewSet, DatasetViewSet, DataPointViewSet

router = routers.DefaultRouter()
router.register('sectors', SectorViewSet, basename='sector')
router.register('indicators', IndicatorViewSet, basename='indicator')
router.register('datasets', DatasetViewSet, basename='dataset')
router.register('datapoints', DataPointViewSet, basename='datapoint')

urlpatterns = [
    path('', include(router.urls)),
]
