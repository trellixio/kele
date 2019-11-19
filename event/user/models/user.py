from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


class EventUserManager(UserManager):
    pass


class User(AbstractUser):
    uid = models.UUIDField(primary_key=True, auto_created=True)

    updated = models.DateTimeField(auto_now=True)

    objects = EventUserManager()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        db_table = 'event.user'
        managed = True
