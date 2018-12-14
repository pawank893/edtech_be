from django.db import models

from edtech.models.questions import Question
from djutil.models import TimeStampedModel
from edtech.models.mixins import DefaultPermissions


class Choice(TimeStampedModel, DefaultPermissions):
    question = models.ForeignKey(Question)
    is_choice_correct = models.BooleanField(default=False)
    choice = models.CharField(max_length=100)

    def __unicode__(self):
        return self.choice
