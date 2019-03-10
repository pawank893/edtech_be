from django.db import models

from edtech.models.questions import Question
from djutil.models import TimeStampedModel
from edtech.models.mixins import DefaultPermissions


class Choice(TimeStampedModel, DefaultPermissions):
    IMAGE = 'Image'
    TEXT = 'Text'
    ChoiceType = (
        (IMAGE, 'Image'),
        (TEXT, 'Text')
    )
    question = models.ForeignKey(Question, related_name='options')
    is_choice_correct = models.BooleanField(default=False)
    choice = models.CharField(max_length=100)
    type = models.CharField(choices=ChoiceType, default=TEXT, max_length=100)

    def __unicode__(self):
        return self.choice
