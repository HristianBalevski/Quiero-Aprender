from django.test import TestCase
from ..models import CustomUser, profile_photo_upload_to
from unittest.mock import Mock
from django.db import IntegrityError
from django.core.exceptions import ValidationError


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


class CustomUserFirstNameLastNameTest(TestCase):
    def test_first_name_last_name(self):
        user = CustomUser.objects.create_user(
            username="user1",
            email="user1@example.com",
            password="password123",
            first_name="Mark",
            last_name="Donovan"
        )
        self.assertEqual(user.first_name, "Mark")
        self.assertEqual(user.last_name, "Donovan")

class CustomUserUsernameValidationTest(TestCase):
    def test_username_length(self):
        valid_user = CustomUser.objects.create_user(
            username="valid_user",
            email="valid@example.com",
            password="password123"
        )
        self.assertEqual(valid_user.username, "valid_user")

        long_username = "a" * 31
        with self.assertRaises(ValidationError):
            user = CustomUser(username=long_username)
            user.full_clean()

    def test_username_uniqueness(self):
        CustomUser.objects.create_user(
            username="unique_user",
            email="unique@example.com",
            password="password123"
        )

        with self.assertRaises(ValidationError):
            duplicate_user = CustomUser(
                username="unique_user",
                email="duplicate@example.com"
            )
            duplicate_user.full_clean()