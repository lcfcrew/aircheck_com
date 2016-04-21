from __future__ import unicode_literals

from django.db import models

from mixins.models import DateMixin


class DataPoint(DateMixin):

    type = models.CharField(max_length=300, null=True, blank=True)
    value = models.DecimalField(max_digits=15, decimal_places=12, null=True, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=12, null=True, blank=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=12, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return str(self.type)
