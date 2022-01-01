from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Branch


class LifeInsuranceTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="ali", password="Aa12345678",
                                                         phoneNumber="09123445656")
        auth_url = "/api/token/"
        authenticate = self.client.post(auth_url, {"username": "ali", "password": "Aa12345678"},
                                        format='json')
        token = authenticate.data["access"]

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.branch = Branch.objects.create(branch_name="test")

    def test_life_insurance_create(self):
        data = {
            "name": "ali",
            "last_name": "alizadeh",
            "email": "ali@ali.com",
            "phoneNumber": "09123445662",
            "age": 32,
            "BMI": 40,
            "smoker": "false",
            "cigarette_count": 0,
            "hookah_count": 0,
            "branch_id": 1
        }

        url = '/api/insurance/create/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
