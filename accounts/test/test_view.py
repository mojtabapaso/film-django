from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Profile
from accounts.models import User


class RegisterAPIViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        url = reverse('accounts:register')
        data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_with_invalid_email(self):
        url = reverse('accounts:register')
        data = {
            'email': 'invalidemail',
            'password': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_mismatched_passwords(self):
        url = reverse('accounts:register')
        data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'password2': 'mismatchedpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LogoutAPIViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='eeeet@email.ocm', password='tgfgfgssword')

    def test_success_logout(self):
        url = reverse('accounts:logout')
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_failed_logout(self):
        url = reverse('accounts:logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ProfileShowAPIViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='eeeet@email.ocm', password='tgfgfgssword')
        self.profile = Profile.objects.create(name='mojtaba', age=21, user=self.user)
        self.url = reverse('accounts:profile')

    def test_profile_show_success(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_show_failure_unauthorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_show_failure_permission_denied(self):
        other_user = User.objects.create_user(email='other@example.com', password='testpass', is_active=True)
        self.client.force_authenticate(user=other_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
