import tweepy


class TwitterAPI(object):
    def __init__(self, consumer_token, consumer_secret, access_token,
                 access_secret):
        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self._api = tweepy.API(auth)

    def search(self, query, max_items=1000):
        """
        Searches Twitter for tweets matching the given query. Results are
        placed in a dictionary using the tweet id as the key.

        :param query: A search string
        :param max_items: The maximum number of tweets to return
        :return: A dictionary of tweets (by "id")
        """
        cursor = tweepy.Cursor(self._api.search, q=query).items(max_items)
        tweets = {}
        for tweet in cursor:
            tweets[tweet.id_str] = {
                'id': tweet.id_str,
                'created': tweet.created_at,
                'location': tweet.coordinates,
                'place': None,
                'text': tweet.text,
                'user': {
                    'id': tweet.user.id,
                    'screen_name': tweet.user.screen_name,
                    'name': tweet.user.name,
                    'location': tweet.user.location,
                },
            }
        return tweets
