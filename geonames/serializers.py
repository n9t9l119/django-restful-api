from rest_framework import serializers

from geonames.models import GeoNames


class GeoNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoNames
        fields = '__all__'

