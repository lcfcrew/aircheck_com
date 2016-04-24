from django.conf import settings
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^api/' + settings.API_VERSION + '/sentiments/twitter/', views.twitter_endpoint),
    url(r'^api/' + settings.API_VERSION + '/sentiments/', views.sentiment_endpoint),
]