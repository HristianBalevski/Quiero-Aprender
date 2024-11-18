from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ImageField


class CustomUser(AbstractUser):
    profile_photo = ImageField(upload_to="profile_photos/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True, max_length=250)
    birth_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.username