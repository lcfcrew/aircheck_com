import os
import tweepy


_CONSUMER_TOKEN = os.environ.get('TWITTER_API_CONSUMER_TOKEN', '')
_CONSUMER_SECRET = os.environ.get('TWITTER_API_CONSUMER_SECRET', '')
_ACCESS_TOKEN = os.environ.get('TWITTER_API_ACCESS_TOKEN', '')
_ACCESS_SECRET = os.environ.get('TWITTER_API_ACCESS_SECRET', '')


class TwitterAPI(object):
    def __init__(self,
                 query,
                 consumer_token=_CONSUMER_TOKEN,
                 consumer_secret=_CONSUMER_SECRET,
                 access_token=_ACCESS_TOKEN,
                 access_secret=_ACCESS_SECRET):
        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.query = query
        self._api = tweepy.API(auth)

    def retrieve(self, max_items=100):
        cursor = tweepy.Cursor(self._api.search, q=self.query).items(max_items)
        return [self._serialize_tweet(t) for t in cursor]

    def retrieve_new(self, tweet_id, max_items=100):
        cursor = tweepy.Cursor(
            self._api.search, q=self.query, since_id=tweet_id).items(max_items)
        return [self._serialize_tweet(t) for t in cursor]

    @staticmethod
    def _serialize_tweet(tweet):
        return {
            'tweet_id': tweet.id_str,
            'created': tweet.created_at,
            # 'location': tweet.coordinates,
            # 'place': None,
            'text': tweet.text,
            # 'user': {
            #     'id': tweet.user.id,
            #     'screen_name': tweet.user.screen_name,
            #     'name': tweet.user.name,
            #     'location': tweet.user.location,
            # },
        }
