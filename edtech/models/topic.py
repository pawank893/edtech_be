from django.db import models

from djutil.models import TimeStampedModel

from edtech.models.mixins import DefaultPermissions
from edtech.models.subject import Subject


class Topic(TimeStampedModel, DefaultPermissions):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject)

    def __unicode__(self):
        return self.name
