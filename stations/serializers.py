import re
from rest_framework import serializers

from stations.models import GasStation, Route


class GasStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasStation
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

    def validate_start_point(self, value):
        if not re.match(r'^\d+\.\d+\s\d+\.\d+$', value):
            raise serializers.ValidationError(
                'Неверный формат координат. Используйте "55.552137 49.487282".'
            )
        return value

    def validate_end_point(self, value):
        if not re.match(r'^\d+\.\d+\s\d+\.\d+$', value):
            raise serializers.ValidationError(
                'Неверный формат координат. Используйте "55.552137 49.487282".'
            )
        return value