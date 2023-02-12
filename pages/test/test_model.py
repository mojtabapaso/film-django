from repository.models import  Film
from ..models import Command
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class TestCommand(TestCase):
    def setUp(self):
        film = Film.objects.create(name='test name film', year_publication='2020-12-12', play_status='published',
                                   Quality='720', product='Iran', language='Parsi', period_time=50.2,
                                   description='test text', is_movie=True, is_serial=False)
        user = User.objects.create(email='test@gmail.com', password='123456test')
        self.command = Command.objects.create(user=user, film=film, text='test text')

    def test_value_model(self):
        command = Command.objects.get(id=1)
        self.assertEqual(self.command.user, command.user)
        self.assertEqual(self.command.film, command.film)
        self.assertEqual(self.command.text, command.text)

    def test_value_in_instance_model(self):
        self.assertFalse(self.command.is_sub_command)
        self.assertFalse(self.command.is_active)
