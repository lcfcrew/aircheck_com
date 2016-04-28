from django.core.management.base import BaseCommand, CommandError
from sentiments import models, azure


class Command(BaseCommand):
    help = 'Analyzes any un-analyzied sentiments'

    def handle(self, *args, **options):
        sentiments = models.Sentiment.objects.filter(sentiment__isnull=True)
        azure_api = azure.AzureAPI()
        azure_data = {
            'documents': [{'id': s.id, 'text': s.text} for s in sentiments]
        }
        sentiment_scores = azure_api.sentiment(azure_data)
        key_phrases = azure_api.key_phrases(azure_data)

        for idx, sentiment in enumerate(sentiments):
            sentiment_score = sentiment_scores['documents'][idx]['score']
            key_phrase_list = key_phrases['documents'][idx]['keyPhrases']

            sentiment.sentiment = sentiment_score
            sentiment.save()

            for phrase in key_phrase_list:
                phrase_obj = models.KeyPhrase.objects.create(
                    sentiment=sentiment, phrase=phrase)
                phrase_obj.save()
