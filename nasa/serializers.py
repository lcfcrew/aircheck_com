from rest_framework import serializers

from .models import DiscretizedDataPoint


class DiscretizedDataPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiscretizedDataPoint
        fields = ('id', 'type', 'value', 'latitude', 'longitude', 'date', )
