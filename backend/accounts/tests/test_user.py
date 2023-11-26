"""Tests about the users.
Can be login, setting/updating value, checking permissions...
"""
import json

from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken

from .. import models

class TestUser(TestCase):
    """Test related to user's information/permissions."""

    def setUp(self) -> None:
        self.client = APIClient()
        self.content_type = "application/json"
        self.information = {
            "email": "ed@elric.com",
            "password": "azerty123azerty123",
            "password1": "azerty123azerty123",
        }
        self.user_ed = models.MyUser.objects.create_user(
            email=self.information["email"],
            password=self.information["password"]
        )
        # self.user_ed.set_password(self.information["password"])
        self.user_ed.save()

        self.access_token = AccessToken.for_user(self.user_ed)

    def test_login_correct_credentials(self):
        """Login in with correct credentials."""
        data = {
            "email": self.information["email"],
            "password": self.information["password"]
        }

        response = self.client.post(
            reverse("users:token_obtain_pair"),
            data=json.dumps(data),
            content_type=self.content_type
        )

        self.assertTrue(response.data.get("access") is not None)
        self.assertTrue(response.data.get("refresh") is not None)
        self.assertEqual(response.status_code, 200)

    def test_login_wrong_credentials(self):
        """Login witn incorrect crendentials."""
        data = {
            "email": self.information["email"],
            "password": self.information["password"] + "wrong_password"
        }

        response = self.client.post(
            reverse("users:token_obtain_pair"),
            data=json.dumps(data),
            content_type=self.content_type
        )

        self.assertTrue(response.data.get("detail") is not None)
        self.assertEqual(
            response.data,
            {"detail": "No active account found with the given credentials"}
        )
        self.assertEqual(response.status_code, 401)

    def test_is_authenticated_working(self):
        """Test the response for the IsAuthenticated permission.
        This permission, forces to user to set all it's optional attribut.
        """
        request = RequestFactory().get(reverse("users:delete_me_please"))

        request.user = self.user_ed
        permissions_check = IsAuthenticated()
        permission = permissions_check.has_permission(request, None)

        self.assertTrue(permission)

    def test_is_authenticated_not_working(self):
        """Test the response for the IsAuthenticated permission.
        Check that user with not all optional field set don't work
        """
        request = RequestFactory().get(reverse("users:delete_me_please"))

        user = models.MyUser.objects.create_user(
            email="al@elric.com",
            password="azerty123azerty123"
        )
        request.user = user
        permissions_check = IsAuthenticated()
        permission = permissions_check.has_permission(request, None)

        self.assertTrue(permission)
