from django.conf import settings
from django.test import TestCase

from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APIClient

from accounts.models import Account

from .models import DataPoint

from . import views

import logging

logger = logging.getLogger(settings.PROJECT_NAME + '-test')


class SensorAPITest(TestCase):

    def setUp(self):
        super(SensorAPITest, self).setUp()

        PASSWORD = 'test'

        self.account = Account.objects.create(email='test@test.com')
        self.account.set_password(PASSWORD)
        self.account.active = True
        self.account.save()

        self.client = APIClient()
        self.client.login(username=self.account.email, password=PASSWORD)

        #self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(Token.objects.get(user=self.account).key)}
        self.header = {}

        views.logger = logger

        self.old_PRODUCTION = settings.PRODUCTION
        settings.PRODUCTION = False

    def tearDown(self):
        settings.PRODUCTION = self.old_PRODUCTION

    def test_create_data_point(self):

        my_type = 'dust'

        self.assertEqual(DataPoint.objects.all().count(), 0)

        json = {'type': my_type, 'value': '5.4535', 'date': '2016-04-20T04:05:59', 'latitude': '11.2342342', 'longitude': '21.534534'}
        response = self.client.post('/api/v1/data_points/', data=json, format='json', **self.header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.content)

        self.assertEqual(DataPoint.objects.all().count(), 1)

        self.assertEqual(DataPoint.objects.get(pk=1).type, my_type)
