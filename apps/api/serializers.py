from rest_framework import serializers
from apps.indicators.models import Sector, Indicator, Region
from apps.datasets.models import Dataset, DataPoint
from apps.insights.models import Insight


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class IndicatorSerializer(serializers.ModelSerializer):
    sector = SectorSerializer(read_only=True)

    class Meta:
        model = Indicator
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'


class DataPointSerializer(serializers.ModelSerializer):
    indicator = IndicatorSerializer(read_only=True)
    region = RegionSerializer(read_only=True)

    class Meta:
        model = DataPoint
        fields = '__all__'


class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = '__all__'
