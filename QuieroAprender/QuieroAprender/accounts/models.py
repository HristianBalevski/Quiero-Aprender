from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ImageField

import os

def profile_photo_upload_to(instance, filename):
    name, ext = os.path.splitext(filename)
    truncated_name = name[:10]
    return f"profile_photos/{truncated_name}{ext}"


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_photo = ImageField(upload_to=profile_photo_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True, max_length=250)
    birth_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.username