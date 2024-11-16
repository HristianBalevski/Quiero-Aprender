from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
import os

from .models import CustomUser


@receiver(pre_save, sender=CustomUser)
def delete_old_profile_photo(sender, instance, **kwargs):
    if instance.pk:
        old_photo = sender.objects.filter(pk=instance.pk).values_list('profile_photo', flat=True).first()
        if old_photo and old_photo != instance.profile_photo.name:
            old_photo_path = os.path.join(instance.profile_photo.storage.location, old_photo)
            if os.path.isfile(old_photo_path):
                os.remove(old_photo_path)



@receiver(post_delete, sender=CustomUser)
def delete_profile_photo_on_user_delete(sender, instance, **kwargs):
    if instance.profile_photo and os.path.isfile(instance.profile_photo.path):
        os.remove(instance.profile_photo.path)