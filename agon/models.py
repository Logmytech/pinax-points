import datetime

from django.core.exceptions import ImproperlyConfigured
from django.db import models

from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from agon.signals import points_awarded


class AwardedPointValue(models.Model):
    """
    Stores a single row for each time a point value is awarded. Can be used
    as an audit trail of when point values were awarded to targets.
    """
    
    # object association (User is special-cased as it's a common case)
    target_user = models.ForeignKey(User, null=True)
    target_content_type = models.ForeignKey(ContentType, null=True)
    target_object_id = models.IntegerField(null=True)
    target_object = generic.GenericForeignKey("target_content_type", "target_object_id")
    
    key = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=datetime.datetime.now)


class TargetStat(models.Model):
    """
    Stores a single row for each target and their stats (points, position and
    level).
    """
    
    # object association (User is special-cased as it's a common case)
    target_user = models.OneToOneField(User, null=True)
    target_content_type = models.ForeignKey(ContentType, null=True)
    target_object_id = models.IntegerField(null=True)
    target_object = generic.GenericForeignKey("target_content_type", "target_object_id")
    
    points = models.IntegerField(default=0)
    position = models.PositiveIntegerField(null=True)
    level = models.PositiveIntegerField(default=1)
    
    class Meta:
        unique_together = [("target_content_type", "target_object_id")]


def award_points(target, key):
    """
    Awards target the point value for key
    """
    apv = AwardedPointValue(key=key)
    if isinstance(target, User):
        apv.target_user = target
        lookup_params = {
            "target_user": target
        }
    else:
        apv.target_object = target
        lookup_params = {
            "target_content_type": apv.target.content_type,
            "target_object_id": apv.target_object_id,
        }
    apv.save()
    
    points_given = lookup_point_value(key)
    
    # @@@ need to check if TargetStat exists first (create it if it does not)
    TargetStat.objects.filter(**lookup_params).update(
        total = models.F("total") + points_given,
    )
    
    points_awarded.send(sender=target.__class__, target=target, key=key)


def lookup_point_value(key):
    try:
        value = settings.AGON_POINT_VALUES[key]
    except AttributeError:
        raise ImproperlyConfigured(
            "You must define 'AGON_POINT_VALUES' in settings"
        )
    except KeyError:
        raise ImproperlyConfigured(
            "You must define a point value for '%s'" % key
        )
    else:
        return value