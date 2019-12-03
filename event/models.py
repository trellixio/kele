import os

from django.db import models
from django.utils.timezone import now

from user.models import User


def _content_file_name(instance, filename):
    filename = "%s_%s" % (now().isoformat(), filename)
    return os.path.join('event', filename)


class EventManager(models.Manager):
    pass


class Event(models.Model):
    # id = models.UUIDField(primary_key=True, auto_created=True, default=generate_uid)
    user = models.ForeignKey(User, related_name="event_set", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=3000, null=True)
    photo = models.ImageField(null=True, upload_to=_content_file_name)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = EventManager()

    def __str__(self):
        return "%s / %s" % (self.name, self.user.username)

    class Meta:
        db_table = "event"
        managed = True
