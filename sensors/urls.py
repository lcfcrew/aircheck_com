from django.conf import settings
from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import DataPointViewSet


router = DefaultRouter()
router.register(r'data_points', DataPointViewSet)

urlpatterns = [
    url(r'^api/' + settings.API_VERSION + '/', include(router.urls)),  # TODO makes sense to have a settings.API_BASE_URL rather than a settings.API_VERSION?
]
