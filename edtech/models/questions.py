from django.db import models

from djutil.models import TimeStampedModel
from edtech.models.mixins import DefaultPermissions
from edtech.models.test_series import TestSeries
from edtech.models.topic import Topic


class Question(TimeStampedModel, DefaultPermissions):
    description = models.TextField()
    diagram = models.CharField(max_length=500, blank=True)
    difficulty_level = models.IntegerField(default=1, blank=True)
    marks = models.FloatField(default=10)
    topic = models.ForeignKey(Topic)
    test_series = models.ForeignKey(TestSeries, null=True, related_name='questions')
    hints = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.description
