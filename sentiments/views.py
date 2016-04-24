import datetime

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from . import models
from . import twitter
from . import azure


_DEFAULT_MAX_ITEMS = 25


def get_ip(request):
    """Returns the IP of the request, accounting for the possibility of being
    behind a proxy.
    """
    ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
    if ip:
        # X_FORWARDED_FOR returns client1, proxy1, proxy2,...
        ip = ip.split(", ")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", "")
    return ip


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def sentiment_endpoint(request):
    """
    List all sentiments or create a new one.
    """

    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['ip_address'] = get_ip(request)
        data['date'] = data.get('date') or datetime.datetime.now()
        serializer = models.SentimentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'GET':
        max_items = request.GET.get('max_items') or _DEFAULT_MAX_ITEMS
        sentiments = models.Sentiment.objects.all()[:max_items]
        serializer = models.SentimentSerializer(sentiments, many=True)
        return JSONResponse(serializer.data)

    return JSONResponse([], status=400)


@csrf_exempt
def twitter_endpoint(request):
    """
    Fetch tweets and tweet data.
    """
    twitter_api = twitter.TwitterAPI("#aircheck")
    azure_api = azure.AzureAPI()

    if request.method == 'PUT':
        try:
            latest_tweet = models.Sentiment.objects.filter(is_tweet=True).latest('date')
            tweet_id = latest_tweet.tweet_id
            twitter_results = twitter_api.retrieve_new(tweet_id)
        except ObjectDoesNotExist:
            twitter_results = twitter_api.retrieve()

        new_tweets = []

        azure_data = {
            'documents': [{'id': k, 'text': v['text']} for
                          k, v in twitter_results.items()]}

        sentiments = azure_api.sentiment(azure_data)
        for tweet in sentiments['documents']:
            tweets[tweet['id']]['sentiment'] = tweet['score']

        return JSONResponse(twitter_results)

    elif request.method == 'GET':
        max_items = request.GET.get('max_items') or _DEFAULT_MAX_ITEMS
        try:
            sentiments = models.Sentiment.objects.filter(is_tweet=True)[:max_items]
            serializer = models.SentimentSerializer(sentiments, many=True)
            return JSONResponse(serializer.data)
        except ObjectDoesNotExist:
            return JSONResponse([])

    return JSONResponse([], status=400)
