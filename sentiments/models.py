from django.db import models
from rest_framework import serializers


class Sentiment(models.Model):
    """
    A statement of health.
    """

    date = models.DateTimeField()
    text = models.CharField(max_length=256)
    latitude = models.DecimalField(
        max_digits=15, decimal_places=12, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=15, decimal_places=12, null=True, blank=True)

    # Organic data
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    # Twitter data
    twitter_id = models.CharField(null=True, blank=True)
    twitter_name = models.CharField(null=True, blank=True)

    # Azure analysis
    language = models.CharField(max_length=64, null=True, blank=True)
    language_iso = models.CharField(max_length=2, null=True, blank=True)
    language_score = models.FloatField(null=True, blank=True)
    sentiment = models.FloatField(null=True, blank=True)

    class Meta(object):
        ordering = ('date',)


class SentimentSerializer(serializers.Serializer):
    """
    A serializer for :class:`~Sentiment`
    """
    # General
    date = serializers.DateTimeField()
    text = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    # Organic
    ip_address = serializers.IPAddressField()

    # Twitter
    twitter_id = serializers.CharField()
    twitter_name = serializers.CharField()

    # Azure
    language = serializers.CharField()
    language_iso = serializers.CharField()
    language_score = serializers.FloatField()
    sentiment = serializers.FloatField()

    def create(self, validated_data):
        return Sentiment.objects.create(**validated_data)


class KeyPhrases(models.Model):
    """
    A list of key phrases associated with a registered Sentiment.
    """
    sentiment = models.ForeignKey(Sentiment, on_delete=models.CASCADE)
