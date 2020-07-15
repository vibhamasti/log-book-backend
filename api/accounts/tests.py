# python imports
import json

# django imports
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED


User = get_user_model()


class UserTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            mobile=1111111111, email="test@api.com", password="password"
        )

        account = User.objects.get(pk=1)
        self.assertEqual(user, account)


class UserRegisterAPITest(APITestCase):
    url = reverse("api:register-register")

    def test_invalid_password(self):
        """
        Test to verify passwords in post call
        """
        user_data = {
            "mobile": 1111111111,
            "email": "test@api.com",
            "password1": "password",
            "password2": "different_password",
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)

    def test_unique_fields(self):
        """
        Test to verify unique fields in post call
        """

        user1_data = {
            "mobile": 1111111111,
            "email": "test@api.com",
            "password1": "password",
            "password2": "password",
        }

        response = self.client.post(self.url, user1_data)
        self.assertEqual(HTTP_201_CREATED, response.status_code)

        user2_data = {
            "mobile": 1111111111,
            "email": "test2@api.com",
            "password1": "password",
            "password2": "password",
        }

        response = self.client.post(self.url, user2_data)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)

        user2_data = {
            "mobile": 2222222222,
            "email": "test@api.com",
            "password1": "password",
            "password2": "password",
        }

        response = self.client.post(self.url, user2_data)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)

    def test_required_fields(self):
        """
        Test to verify required fields
        """
        user_data = {
            "email": "test@api.com",
            "password1": "password",
            "password2": "password",
        }

        response = self.client.post(self.url, user_data)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)

        user_data = {
            "mobile": 1111111111,
            "password1": "password",
            "password2": "password",
        }

        response = self.client.post(self.url, user_data)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)

    def test_user_register(self):
        """
        Test to verify post call with valid user data.
        """
        user_data = {
            "mobile": 1111111111,
            "email": "test@api.com",
            "password1": "password",
            "password2": "password",
        }

        response = self.client.post(self.url, user_data)
        self.assertEqual(HTTP_201_CREATED, response.status_code)
        self.assertTrue("token" in json.loads(response.content))


class UserLoginAPITest(APITestCase):
    url = reverse("api:login-login")

    def setUp(self):
        self.user = User.objects.create(
            mobile=1111111111, email="test@api.com", password="password"
        )

    def test_wrong_password(self):
        """
        Test for checking if password is entered wrong.
        """
        user_data = {"mobile": 1111111111, "password": "wrong_password"}

        response = self.client.post(self.url, user_data)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)

    def test_required_fields(self):
        """
        Test for checking if required fields are entered.
        """

        user_data = {"mobile": 1111111111}
        response = self.client.post(self.url, user_data)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)

        user_data = {"password": "password"}
        response = self.client.post(self.url, user_data)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)

        user_data = {"email": "test@api.com", "password": "password"}
        response = self.client.post(self.url, user_data)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)
