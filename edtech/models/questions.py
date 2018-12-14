from django.db import models

from djutil.models import TimeStampedModel
from edtech.models.mixins import DefaultPermissions
from edtech.models.test_series import TestSeries
from edtech.models.topic import Topic


class Question(TimeStampedModel, DefaultPermissions):
    description = models.TextField()
    diagram = models.CharField(max_length=500)
    difficulty_level = models.IntegerField(default=1)
    marks = models.FloatField()
    topic = models.ForeignKey(Topic)
    test_series = models.ForeignKey(TestSeries, null=True)
    hints = models.TextField(null=True)

    def __unicode__(self):
        return self.description
