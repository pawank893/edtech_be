from django.contrib.auth.models import User
from django.db import models

from edtech.models.choices import Choice
from edtech.models.questions import Question

from djutil.models import TimeStampedModel
from edtech.models.mixins import DefaultPermissions


class UserQuestionAnswer(TimeStampedModel, DefaultPermissions):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    choice = models.ForeignKey(Choice)
    is_correct = models.BooleanField(default=False)
    session_end = models.BooleanField(default=False)
