from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User  # Use this instead of authtoken.admin.User

class RegisterViewTest(APITestCase):

    def test_register_user(self):
        print("✅ user.tests.py loaded")
        url = reverse('register')  # Make sure you name your URL pattern as 'register'
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'test@example.com'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_login_user(self):

        self.user = User.objects.create_user(username='testuser', password='test123')
        print("✅ user.tests.py loaded")
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'test123'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_user(self):
        print("✅ user.tests.py loaded")

        # 1. Create user
        user = User.objects.create_user(username='testuser', password='test123')

        # 2. Generate token
        token = Token.objects.create(user=user)

        # 3. Set auth header
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # 4. Call logout endpoint
        url = reverse('logout')
        response = self.client.post(url)

        # 5. Check response
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # or 200 if you prefer