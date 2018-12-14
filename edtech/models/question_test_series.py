from django.db import models

from edtech.models.questions import Question

from djutil.models import TimeStampedModel
from edtech.models.mixins import DefaultPermissions
from edtech.models.test_series import TestSeries


class QuestionTestSeries(TimeStampedModel, DefaultPermissions):
    question = models.ForeignKey(Question)
    test_series = models.ForeignKey(TestSeries)
