from django.db import models

from xlib.utils import generate_uid


class CommentManager(models.Manager):
    pass


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=generate_uid)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE)
    user = models.ForeignKey('event_user.User', on_delete=models.CASCADE)
    message = models.CharField(max_length=130)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CommentManager()

    class Meta:
        db_table = "event.comment"
        managed = True
