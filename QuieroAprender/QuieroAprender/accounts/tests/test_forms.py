from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from QuieroAprender.accounts.forms import (
    CustomUserCreationForm,
    CustomUserUpdateForm,
    LoginForm,
)
from QuieroAprender.accounts.models import CustomUser


class TestCustomUserCreationForm(TestCase):
    def test_valid_data(self):

        form = CustomUserCreationForm(
            data={
                "username": "testuser",
                "email": "testuser@example.com",
                "password1": "StrongPassword123!",
                "password2": "StrongPassword123!",
                "bio": "I love learning Spanish!",
                "birth_date": "2000-01-01",
            }
        )
        self.assertTrue(form.is_valid())

    def test_password_mismatch(self):

        form = CustomUserCreationForm(
            data={
                "username": "testuser",
                "email": "testuser@example.com",
                "password1": "StrongPassword123!",
                "password2": "WrongPassword123!",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_invalid_email(self):

        form = CustomUserCreationForm(
            data={
                "username": "testuser",
                "email": "invalid-email",
                "password1": "StrongPassword123!",
                "password2": "StrongPassword123!",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)


class TestCustomUserUpdateForm(TestCase):
    def test_valid_update(self):

        user = CustomUser.objects.create_user(
            username="existinguser",
            email="existing@example.com",
            password="password123",
        )
        form = CustomUserUpdateForm(
            data={
                "email": "updated@example.com",
                "first_name": "UpdatedName",
                "last_name": "UpdatedLastName",
                "bio": "Updated bio",
                "birth_date": "1990-01-01",
            },
            instance=user,
        )
        self.assertTrue(form.is_valid())

    def test_invalid_image_upload(self):

        user = CustomUser.objects.create_user(
            username="existinguser",
            email="existing@example.com",
            password="password123",
        )
        invalid_image = SimpleUploadedFile(
            "large_image.jpg", b"x" * (10 * 1024 * 1024), content_type="image/jpeg"
        )
        form = CustomUserUpdateForm(
            data={
                "email": "updated@example.com",
                "first_name": "UpdatedName",
                "last_name": "UpdatedLastName",
                "bio": "Updated bio",
                "birth_date": "1990-01-01",
            },
            files={"profile_photo": invalid_image},
            instance=user,
        )
        self.assertFalse(form.is_valid())
        self.assertIn("profile_photo", form.errors)


class TestLoginForm(TestCase):
    def test_valid_login(self):

        user = CustomUser.objects.create_user(
            username="loginuser", email="loginuser@example.com", password="password123"
        )
        form = LoginForm(data={"username": "loginuser", "password": "password123"})
        self.assertTrue(form.is_valid())

    def test_invalid_login(self):

        form = LoginForm(data={"username": "wronguser", "password": "wrongpassword"})
        self.assertFalse(form.is_valid())
