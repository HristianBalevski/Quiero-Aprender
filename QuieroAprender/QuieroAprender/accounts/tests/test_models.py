from django.test import TestCase
from ..models import CustomUser, profile_photo_upload_to
from unittest.mock import Mock
from django.db import IntegrityError


class ProfilePhotoUploadToTest(TestCase):
    def test_profile_photo_upload_to(self):
        mock_instance = Mock()
        filename = "verylongfilename.png"
        upload_path = profile_photo_upload_to(mock_instance, filename)

        self.assertEqual(upload_path, "profile_photos/verylongfi.png")


class CustomUserModelTest(TestCase):
    def test_email_uniqueness(self):
        CustomUser.objects.create_user(
            username="user1", email="test@example.com", password="password123"
        )

        with self.assertRaises(IntegrityError):
            CustomUser.objects.create_user(
                username="user2", email="test@example.com", password="password123"
            )


class CustomUserProfilePhotoTest(TestCase):
    def test_profile_photo_field(self):
        user = CustomUser.objects.create_user(
            username="user1", email="user1@example.com", password="password123"
        )
        user.profile_photo = "profile_photos/sample.png"
        user.save()

        self.assertEqual(user.profile_photo, "profile_photos/sample.png")
