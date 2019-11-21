from django.db import models

from event.user.models import User
from event.xlib.utils import generate_uid


class EventManager(models.Manager):
    pass


class Event(models.Model):
    user = models.ForeignKey(User, related_name="event_set", on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, auto_created=True, default=generate_uid)
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=3000, null=True)
    photo = models.URLField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = EventManager()

    def __str__(self):
        return "%s / %s" % (self.name, self.user.username)

    class Meta:
        db_table = "event.event "
        managed = True
