from django.db.models import fields
from rest_framework import serializers
from rootapp.models import Country, Region, City


class CountrySerializer(serializers.ModelSerializer):
    """Serializer for Country objects"""

    class Meta:
        model = Country
        fields = ('id', 'name', 'latitude', 'longitude', 'type')
        read_only_fields = ('id', 'type',)


class RegionSerializer(serializers.ModelSerializer):
    """Serializer for Region objects"""

    class Meta:
        model = Region
        fields = ('id', "country", "name", 'latitude', 'longitude', "type")
        read_only_fields = ('id', 'type',)


class CitySerializer(serializers.ModelSerializer):
    """Serializer for City objects"""

    class Meta:
        model = City
        fields = ('id', "region", "name", 'latitude', 'longitude', "type")
        read_only_fields = ('id', 'type',)


class NameFilterSerializer(serializers.Serializer):
    countries = CountrySerializer(many=True)
    regions = RegionSerializer(many=True)
    cities = CitySerializer(many=True)