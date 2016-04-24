from decimal import Decimal

from django.conf import settings

from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from .models import DiscretizedDataPoint
from .serializers import DiscretizedDataPointSerializer


import logging

logger = logging.getLogger(settings.PROJECT_NAME + '-test')


class DiscretizedDataPointViewSet(viewsets.ModelViewSet):
    queryset = DiscretizedDataPoint.objects.all()
    serializer_class = DiscretizedDataPointSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = ()

    def list(self, request, *args, **kwargs):
        discretized_data_points = DiscretizedDataPoint.objects.all()

        if 'longitude_start' in request.GET:
            discretized_data_points = discretized_data_points.filter(longitude__gte=request.GET.get('longitude_start'))
        if 'longitude_end' in request.GET:
            discretized_data_points = discretized_data_points.filter(longitude__lte=request.GET.get('longitude_end'))
        if 'latitude_start' in request.GET:
            discretized_data_points = discretized_data_points.filter(longitude__gte=request.GET.get('latitude_start'))
        if 'latitude_end' in request.GET:
            discretized_data_points = discretized_data_points.filter(longitude__lte=request.GET.get('latitude_end'))

        if 'type' in request.GET:
            discretized_data_points = discretized_data_points.filter(type=request.GET.get('type'))

        return Response(DiscretizedDataPointSerializer(discretized_data_points, many=True).data)
