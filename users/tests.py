from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.


class RegisterationTestCase(APITestCase):

    def test_registeration(self):
        data = {"username": "davood", "password":"Aa12345678", "phoneNumber":"09123455678"}
        response = self.client.post("/api/user/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginTestCase(APITestCase):
    def test_login(self):
        url = "/api/token/"

        user = get_user_model().objects.create_user(username="alireza", password="Aa12345678",
                                                    phoneNumber="09123445567")

        response = self.client.post(url, {"username":"alireza", "password":"Aa12345678"}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ChangePasswordTestCase(APITestCase):
    def test_password_change(self):
        auth_url = "/api/token/"
        change_url = reverse('users:change_password')

        user = get_user_model().objects.create_user(username="alireza", password="Aa12345678",
                                                    phoneNumber="09123445567")

        authenticate = self.client.post(auth_url, {"username":"alireza", "password":"Aa12345678"}, format='json')
        token = authenticate.data["access"]

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        data = {"old_password": "Aa12345678", "password":"aA12345678", "password2":"aA12345678"}
        response = self.client.put(change_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
