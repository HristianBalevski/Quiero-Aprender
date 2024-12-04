from django.conf import settings
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    attendees = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="events"
    )

    def __str__(self):
        return self.title
