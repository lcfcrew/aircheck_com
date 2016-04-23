from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework.parsers import JSONParser

from . import models
from . import twitter


@csrf_exempt
def sentiment_collection(request):
    """
    List all sentiments or create a new one.
    """

    if request.method is 'POST':
        data = JSONParser().parse(request)
        serializer = models.SentimentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method is 'UPDATE':
        # Call Twitter
        twitter_api = twitter.TwitterAPI(
            consumer_token, consumer_secret, access_token, access_secret)

    elif request.method is 'GET':
        sentiments = models.Sentiment.objects.all()
        serializer = models.SentimentSerializer(sentiments, many=True)
        return JsonResponse(serializer.data)
