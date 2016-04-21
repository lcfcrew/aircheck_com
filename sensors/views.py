from django.conf import settings

from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from .models import DataPoint
from .serializers import DataPointSerializer


import logging

logger = logging.getLogger(settings.PROJECT_NAME + '-test')


class DataPointViewSet(viewsets.ModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = ()
