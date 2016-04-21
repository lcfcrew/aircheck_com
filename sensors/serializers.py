from rest_framework import serializers

from .models import DataPoint


class DataPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataPoint
        fields = ('id', 'type', 'value', 'latitude', 'longitude', 'date', )
