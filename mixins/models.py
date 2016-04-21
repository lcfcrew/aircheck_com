from django.db import models


class DateMixin(models.Model):
    """ Adds tracking for the times when an object was created and last updated """

    class Meta:
        abstract = True
        ordering = ['-date_created']

    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
