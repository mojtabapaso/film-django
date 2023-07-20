from django.test import TestCase
from django.urls import resolve, reverse
from rest_framework.test import APIClient
from accounts.models import User
from repository.models import Film, Genre
from ..models import Command
from ..views import FilmAPIView, FilmDetailAPIView, FilterTypeAPIView, FilmSearchAPIView, CreateCommandAPIView, \
    CreateAnswerCommandAPIView, FilterGenreAPIView


class FilmAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_view_success(self):
        url = "/"
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func.view_class, FilmAPIView)

    def test_view_bad_not_found(self):
        response = self.client.get("/test/")
        self.assertEqual(response.status_code, 404)


class FilmDetailAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.film = Film.objects.create(name='test name film', year_publication='2020-12-12', play_status='published',
                                        Quality='720', product='Iran', language='Parsi', period_time=50.2,
                                        description='test text', is_movie=True, is_serial=False, slug="slug_test")

    def test_view_success(self):
        url = reverse("pages:detail", args=['slug_test'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func.view_class, FilmDetailAPIView)

    def test_view_bad_not_found(self):
        url = reverse("pages:detail", args=['slug'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class FilmSearchAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_view_success(self):
        url = reverse("pages:search")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func.view_class, FilmSearchAPIView)


class FilterTypeAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_view_success(self):
        url = reverse("pages:filter")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func.view_class, FilterTypeAPIView)


class FilterGenreAPIViewTest(TestCase):
    def setUp(self):
        Genre.objects.create(name='test', slug='slug_genre_test')
        self.client = APIClient()

    def test_view_success(self):
        url = reverse("pages:genre", args=["slug_genre_test"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func.view_class, FilterGenreAPIView)


class CreateCommandAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Genre.objects.create(name='test', slug='slug_genre_test')
        self.film = Film.objects.create(name='test name film', year_publication='2020-12-12', play_status='published',
                                        Quality='720', product='Iran', language='Parsi', period_time=50.2,
                                        description='test text', is_movie=True, is_serial=False, slug="slug_test")
        self.user = User.objects.create_user(email='test@email.ocm', password='test_password')

    def test_view_success(self):
        self.client.force_authenticate(user=self.user)
        data_json = {"text": "test_text", "score": "1"}
        url = reverse("pages:add-commend", args=["slug_test"])
        response = self.client.post(url, data=data_json)
        self.assertEqual(resolve(url).func.view_class, CreateCommandAPIView)
        self.assertEqual(response.status_code, 200)

    def test_view_bad_request(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("pages:add-commend", args=["slug_test"])
        response = self.client.post(url)
        self.assertEqual(resolve(url).func.view_class, CreateCommandAPIView)
        self.assertEqual(response.status_code, 400)

    def test_view_bad_unauthenticated(self):
        url = reverse("pages:add-commend", args=["slug_test"])
        response = self.client.post(url)
        self.assertEqual(resolve(url).func.view_class, CreateCommandAPIView)
        self.assertEqual(response.status_code, 401)

    def test_view_bad_not_found(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("pages:add-commend", args=["m"])
        response = self.client.post(url)
        self.assertEqual(resolve(url).func.view_class, CreateCommandAPIView)
        self.assertEqual(response.status_code, 404)


class CreateAnswerCommandAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        film = Film.objects.create(name='test name film', year_publication='2020-12-12', play_status='published',
                                   Quality='720', product='Iran', language='Parsi', period_time=50.2,
                                   description='test text', is_movie=True, is_serial=False, slug="slug_film_test")
        self.user = User.objects.create(email='test@gmail.com', password='123456test')
        self.command = Command.objects.create(user=self.user, film=film, text='test text')

    def test_success(self):
        self.client.force_authenticate(user=self.user)
        data_json = {"text": "test_text"}
        url = reverse("pages:answer-commend", args=["slug_film_test", 1])
        response = self.client.post(url, data=data_json)
        self.assertEqual(resolve(url).func.view_class, CreateAnswerCommandAPIView)
        self.assertEqual(response.status_code, 200)

    def test_view_bad_request(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("pages:answer-commend", args=["slug_film_test", 1])
        response = self.client.post(url)
        self.assertEqual(resolve(url).func.view_class, CreateAnswerCommandAPIView)
        self.assertEqual(response.status_code, 400)

    def test_view_unauthenticated(self):
        data_json = {"text": "test_text"}
        url = reverse("pages:answer-commend", args=["slug_film_test", 1])
        response = self.client.post(url, data=data_json)
        self.assertEqual(resolve(url).func.view_class, CreateAnswerCommandAPIView)
        self.assertEqual(response.status_code, 401)

    def test_view_bad_not_found(self):
        self.client.force_authenticate(user=self.user)
        data_json = {"text": "test_text"}
        url = reverse("pages:answer-commend", args=["slug_film_test_not_found", 6])
        response = self.client.post(url, data=data_json)
        self.assertEqual(resolve(url).func.view_class, CreateAnswerCommandAPIView)
        self.assertEqual(response.status_code, 404)
