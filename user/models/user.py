from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models

from xlib.utils import generate_uid


class EventUserManager(UserManager):
    pass


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, auto_created=True, default=generate_uid)

    updated = models.DateTimeField(auto_now=True)

    objects = EventUserManager()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        db_table = 'event.user'
        unique_together = (('email',),)
        managed = True
