from rest_framework.test import APITestCase

from user.models import User


class AuthTestCase(APITestCase):
    def setUp(self) -> None:
        self.data = {
            "first_name": "youyou",
            "last_name": "corentin",
            "username": "youyou",
            "email": "youyou@yopmail.com",
            "password": "123456789"
        }

    def test_create_account(self):
        response = self.client.post('/v1/account/', data=self.data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('success', response.json())

    def test_auth(self):
        User.objects.create_user(**self.data)
        response = self.client.post('/v1/auth/', data=self.data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json())

    def test_logout(self):
        # Retrieve token
        User.objects.create_user(**self.data)
        response = self.client.post('/v1/auth/', data=self.data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json())
        token = response.json()['token']

        # Logout
        self.client.credentials(HTTP_AUTHORIZATION='Bearer %s' % token)
        response = self.client.post('/v1/logout/', data=None, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json())
