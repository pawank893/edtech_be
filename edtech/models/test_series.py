from django.db import models

from djutil.models import TimeStampedModel

from edtech.models import SeriesType
from edtech.models.mixins import DefaultPermissions


class TestSeries(TimeStampedModel, DefaultPermissions):
    name = models.CharField(max_length=100)
    series_type = models.CharField(choices=SeriesType.SeriesType.TYPES, max_length=100)
    is_paid = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
