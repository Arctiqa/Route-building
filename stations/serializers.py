from rest_framework import serializers

from stations.models import GasStation, Route, Refueling


class GasStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasStation
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class RefuelingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refueling
        fields = '__all__'
