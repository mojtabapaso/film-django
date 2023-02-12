from django.test import TestCase
from ..models import User, Profile


class TestUser(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@email.ocm', password='test=password')
        self.super_user = User.objects.create_superuser(email='testsuper@email.ocm', password='test=password')

    def test_value_model(self):
        user = User.objects.get(id=1)
        user_super = User.objects.get(id=2)
        self.assertEqual(user.email, self.user.email)
        self.assertEqual(user.password, self.user.password)
        self.assertFalse(user.is_admin)
        self.assertTrue(user.is_active)
        self.assertEqual(self.super_user.email, user_super.email)
        self.assertTrue(self.super_user.is_admin)


class TestProfile(TestCase):
    def setUp(self):
        user = User.objects.create(email='eeeet@email.ocm', password='tgfgfgssword')
        self.profile = Profile.objects.create(name='mojtaba', age=21, user=user)
        # self.profile = Profile.objects.get(user=user)
        # self.profile.update(name='mojtaba', age=21)

    def test_value_in_model(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(self.profile.name, profile.name)
        self.assertEqual(self.profile.age, profile.age)
        self.assertEqual(self.profile.user, profile.user)
