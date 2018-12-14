from django.db import models

from djutil.models import TimeStampedModel
from edtech.models.mixins import DefaultPermissions


class SeriesType(TimeStampedModel, DefaultPermissions):

    class SeriesType(object):
        FLASH_TEST = "flash_test"
        TEST_SERIES = "test_series"
        MOCK_TEST = "mock_test"

        TYPES = tuple([(x, x) for x in [FLASH_TEST, TEST_SERIES, MOCK_TEST]])

    series_type = models.CharField(max_length=100, choices=SeriesType.TYPES)

    def __unicode__(self):
        return self.series_type
