from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

TEST_PASSWORD = "Str0ngP@ssword!"


class AccountViewsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@example.com", password=TEST_PASSWORD
        )
        self.other_user = get_user_model().objects.create_user(
            username="otheruser", email="other@example.com", password=TEST_PASSWORD
        )
        self.client.login(username="testuser", password=TEST_PASSWORD)

    def test_register_view(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": TEST_PASSWORD,
            "password2": TEST_PASSWORD,
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, 302)

    def test_login_view(self):
        data = {
            "username": "testuser",
            "password": TEST_PASSWORD,
        }
        response = self.client.post(reverse("login"), data)
        self.assertEqual(response.status_code, 302)

    def test_update_profile_view(self):
        data = {
            "email": "updated@example.com",
            "first_name": "Updated",
            "last_name": "User",
        }
        response = self.client.post(
            reverse("update", kwargs={"username": self.user.username}), data
        )
        self.assertEqual(response.status_code, 302)

    def test_update_profile_view_no_permission(self):
        self.client.login(username="otheruser", password=TEST_PASSWORD)
        data = {
            "email": "updated@example.com",
        }
        response = self.client.post(
            reverse("update", kwargs={"username": self.user.username}), data
        )
        self.assertEqual(response.status_code, 403)

    def test_delete_profile_view(self):
        response = self.client.post(
            reverse("delete", kwargs={"username": self.user.username})
        )
        self.assertEqual(response.status_code, 302)

    def test_delete_profile_view_no_permission(self):
        self.client.login(username="otheruser", password=TEST_PASSWORD)
        response = self.client.post(
            reverse("delete", kwargs={"username": self.user.username})
        )
        self.assertEqual(response.status_code, 403)

    def test_profile_view(self):
        response = self.client.get(
            reverse("profile", kwargs={"username": self.user.username})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)

    def test_login_required_redirect(self):
        self.client.logout()
        response = self.client.get(
            reverse("update", kwargs={"username": self.user.username})
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse("login")))

    def test_invalid_registration(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": TEST_PASSWORD,
            "password2": "DifferentPassword",
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The two password fields didn’t match.")
