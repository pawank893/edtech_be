from django.db import models

from edtech.constants.custom_permissions import CustomPermissions


class DefaultPermissions(models.Model):
    class Meta:
        abstract = True
        default_permissions = (CustomPermissions.ADD, CustomPermissions.CHANGE,
                               CustomPermissions.READ, CustomPermissions.DELETE)
