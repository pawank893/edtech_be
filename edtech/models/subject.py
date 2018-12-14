from django.db import models

from djutil.models import TimeStampedModel
from edtech.models.mixins import DefaultPermissions


class Subject(TimeStampedModel, DefaultPermissions):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
