from django.db import models
from rest_framework import serializers


class Sentiment(models.Model):
    """
    A statement of health.
    """

    created = models.DateTimeField()
    text = models.CharField(max_length=256)
    latitude = models.DecimalField(
        max_digits=15, decimal_places=12, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=15, decimal_places=12, null=True, blank=True)

    # Organic data
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    # Twitter data
    is_tweet = models.BooleanField(default=False) # TODO: require other fields
    tweet_id = models.CharField(max_length=128, null=True, blank=True)
    twitter_user = models.CharField(max_length=128, null=True, blank=True)

    # Azure analysis
    language = models.CharField(max_length=64, null=True, blank=True)
    language_iso = models.CharField(max_length=2, null=True, blank=True)
    language_score = models.FloatField(null=True, blank=True)
    sentiment = models.FloatField(null=True, blank=True)

    class Meta(object):
        ordering = ('created',)


class SentimentSerializer(serializers.Serializer):
    """
    A serializer for :class:`~Sentiment`
    """
    # General
    created = serializers.DateTimeField(required=False)
    text = serializers.CharField()
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)

    # Organic
    ip_address = serializers.IPAddressField(required=False)

    # Twitter
    is_tweet = serializers.BooleanField(default=False)
    tweet_id = serializers.CharField(required=False)
    twitter_user = serializers.CharField(required=False)

    # Azure
    language = serializers.CharField(required=False)
    language_iso = serializers.CharField(required=False)
    language_score = serializers.FloatField(required=False)
    sentiment = serializers.FloatField(required=False)

    def create(self, validated_data):
        return Sentiment.objects.create(**validated_data)


# class KeyPhrases(models.Model):
#     """
#     A list of key phrases associated with a registered Sentiment.
#     """
#     sentiment = models.ForeignKey(Sentiment, on_delete=models.CASCADE)
