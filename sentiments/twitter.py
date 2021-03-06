import os
import tweepy
from geopy import geocoders

from . import _DEFAULT_MAX_ITEMS


_CONSUMER_TOKEN = os.environ.get('TWITTER_API_CONSUMER_TOKEN', '')
_CONSUMER_SECRET = os.environ.get('TWITTER_API_CONSUMER_SECRET', '')
_ACCESS_TOKEN = os.environ.get('TWITTER_API_ACCESS_TOKEN', '')
_ACCESS_SECRET = os.environ.get('TWITTER_API_ACCESS_SECRET', '')
_BING_API_KEY = os.environ.get('BING_API_KEY', '')


def _get_lat_long(tweet):
    geolocator = geocoders.Bing(_BING_API_KEY)
    location = None
    if tweet.coordinates:
        print('Tweet coordinates: %s' % tweet.coordinates)
        return tweet.coordinates
    elif tweet.place:
        print('Tweet place: %s' % tweet.place)
        location = geolocator.geocode(tweet.place.full_name)
    elif tweet.user.location.encode('ascii', 'ignore'):
        print('User location: %s' % tweet.user.location.encode('ascii', 'ignore'))
        location = geolocator.geocode(tweet.user.location.encode('ascii', 'ignore'))
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


class TwitterAPI(object):
    def __init__(self,
                 query,
                 consumer_token=_CONSUMER_TOKEN,
                 consumer_secret=_CONSUMER_SECRET,
                 access_token=_ACCESS_TOKEN,
                 access_secret=_ACCESS_SECRET):
        auth = tweepy.AppAuthHandler(consumer_token, consumer_secret)
        self.query = query
        self._api = tweepy.API(auth)

    def retrieve(self, max_items=_DEFAULT_MAX_ITEMS):
        cursor = tweepy.Cursor(
            self._api.search, q=self.query).items(max_items)
        return [self._serialize_tweet(t) for t in cursor]

    def retrieve_new(self, tweet_id, max_items=_DEFAULT_MAX_ITEMS):
        cursor = tweepy.Cursor(
            self._api.search, q=self.query, since_id=tweet_id).items(max_items)
        return [self._serialize_tweet(t) for t in cursor]

    @staticmethod
    def _serialize_tweet(tweet):
        latitude, longitude = _get_lat_long(tweet)
        return {
            'created': tweet.created_at,
            'text': tweet.text.encode('ascii', 'ignore'),
            'tweet_id': tweet.id_str,
            'twitter_user_id': tweet.user.id_str,
            'twitter_user': tweet.user.screen_name,
            'latitude': latitude,
            'longitude': longitude,
            'language': tweet.lang,
            # 'location': tweet.coordinates,
            # 'place': None,
            # 'user': {
            #     'id': tweet.user.id,
            #     'screen_name': tweet.user.screen_name,
            #     'name': tweet.user.name,
            #     'location': tweet.user.location,
            # },
        }
