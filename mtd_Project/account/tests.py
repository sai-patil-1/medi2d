from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from .views import user_login  # Make sure you import the user_login view
from django.contrib.messages import get_messages  # Import get_messages

class AccountAppTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user)

    def test_user_login(self):
        response = self.client.post(reverse("login"), {"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(response.url, reverse("dashboard"))  # Adjust this URL as per your configuration

    # Invalid LoginDoesnt redirect, it shows form error
    def test_user_login_invalid_credentials(self):
        response = self.client.post(reverse("login"), {"username": "testuser", "password": "wrongpassword"})
        self.assertEqual(response.status_code, 200)  # Expecting a status code of 200 (login page)
        # self.assertContains(response, "Invalid login")  # Check for the error message

    def test_dashboard_authenticated(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dashboard")

    def test_dashboard_unauthenticated(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)  # Redirects to login page


    def test_edit_profile(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("edit"), {"first_name": "New", "last_name": "Name"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profile updated successfully")

    def test_edit_profile_unauthenticated(self):
        response = self.client.post(reverse("edit"), {"first_name": "New", "last_name": "Name"})
        self.assertEqual(response.status_code, 302)  # Redirects to login page



