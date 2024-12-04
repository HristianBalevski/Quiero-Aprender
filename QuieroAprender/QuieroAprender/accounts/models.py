import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ImageField


def profile_photo_upload_to(instance, filename):
    name, ext = os.path.splitext(filename)
    truncated_name = name[:10]
    return f"profile_photos/{truncated_name}{ext}"


from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    profile_photo = ImageField(upload_to=profile_photo_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True, max_length=250)
    birth_date = models.DateField(null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
