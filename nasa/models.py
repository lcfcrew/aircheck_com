from __future__ import unicode_literals

from django.db import models

from mixins.models import DateMixin


class NasaDataFile(DateMixin):

    collection_short_name = models.CharField(max_length=300, null=True, blank=True)
    collection_long_name = models.CharField(max_length=300, null=True, blank=True)
    hdf = models.FileField(null=True, blank=True)
    xml = models.FileField(null=True, blank=True)
    bounding_west = models.DecimalField(max_digits=15, decimal_places=12, null=True, blank=True)
    bounding_north = models.DecimalField(max_digits=15, decimal_places=12, null=True, blank=True)
    bounding_east = models.DecimalField(max_digits=15, decimal_places=12, null=True, blank=True)
    bounding_south = models.DecimalField(max_digits=15, decimal_places=12, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return str(self.collection_short_name)


class DiscretizedDataPoint(DateMixin):

    type = models.CharField(max_length=300, null=True, blank=True)
    value = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    latitude = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    longitude = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return str(self.type)
