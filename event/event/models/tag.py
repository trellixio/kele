from django.db import models

from event.xlib.utils import generate_uid


class EventTagManager(models.Manager):
    pass


class EventTag(models.Model):
    events = models.ManyToManyField('event_event.Event', related_name='tags')
    id = models.UUIDField(auto_created=True, primary_key=True, default=generate_uid)
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = EventTagManager()

    def __str__(self):
        return "%s" % self.name

    class Meta:
        db_table = "event.event_tag"
        managed = True
