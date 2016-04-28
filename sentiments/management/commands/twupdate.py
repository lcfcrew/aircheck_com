from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from sentiments import models, twitter


class Command(BaseCommand):
    help = 'Fetches new tweets'

    def handle(self, *args, **options):

        twitter_api = twitter.TwitterAPI("air quality")

        try:
            latest_tweet = models.Sentiment.objects.filter(is_tweet=True).latest('created')
            tweet_id = latest_tweet.tweet_id
            tweets = twitter_api.retrieve_new(tweet_id, 100)
        except ObjectDoesNotExist:
            tweets = twitter_api.retrieve(100)

        # Serialize
        deserializer = models.SentimentSerializer()

        for idx, tweet_data in enumerate(tweets):
            tweet = deserializer.create(tweet_data)
            tweet.is_tweet = True
            tweet.save()