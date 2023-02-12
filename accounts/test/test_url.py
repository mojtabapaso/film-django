from django.test import SimpleTestCase
from django.urls import resolve
from rest_framework.reverse import reverse
from .. import views


class TestURLAccounts(SimpleTestCase):
    def test_url_register(self):
        url = reverse('accounts:register')
        view = resolve(url)
        self.assertEqual(view.func.view_class.__name__, views.RegisterAPIView.__name__)

    def test_url_login(self):
        url = reverse('accounts:login')
        view = resolve(url)
        self.assertEqual(view.func.view_class.__name__, views.LoginAPIView.__name__)

    def test_url_logout(self):
        url = reverse('accounts:logout')
        view = resolve(url)
        self.assertEqual(view.func.view_class.__name__, views.LogoutAPIView.__name__)

    def test_url_profile(self):
        url = reverse('accounts:profile')
        view = resolve(url)
        self.assertEqual(view.func.view_class.__name__, views.ProfileShowAPIView.__name__)

    def test_url_update_profile(self):
        url = reverse('accounts:update_profile', kwargs={'pk': 1})
        view = resolve(url)
        self.assertEqual(view.func.view_class.__name__, views.ProfileUpdateAPIView.__name__)
