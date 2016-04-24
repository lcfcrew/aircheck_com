from django.conf import settings
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^api/' + settings.API_VERSION + '/sentiments/twitter/new/', views.new_tweets),
    url(r'^api/' + settings.API_VERSION + '/sentiments/twitter/', views.tweets),
    url(r'^api/' + settings.API_VERSION + '/sentiments/', views.sentiments),
]
