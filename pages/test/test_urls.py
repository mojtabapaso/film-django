from django.test import SimpleTestCase
from django.urls import resolve
from rest_framework.reverse import reverse
from .. import views


class PagesUrlsTest(SimpleTestCase):
    def test_home_url(self):
        url = reverse('pages:home')
        view = resolve(url)
        self.assertIs(view.func.view_class.__name__, views.FilmAPIView.__name__)

    def test_detail_url(self):
        url = reverse('pages:detail', kwargs={'slug_film': 'test-slug'})
        view = resolve(url)
        self.assertIs(view.func.view_class.__name__, views.FilmDetailAPIView.__name__)

    def test_search_url(self):
        url = reverse('pages:search')
        view = resolve(url)
        self.assertIs(view.func.view_class.__name__, views.FilmSearchAPIView.__name__)

    def test_filter_url(self):
        url = reverse('pages:filter')
        view = resolve(url)
        self.assertIs(view.func.view_class.__name__, views.FilterTypeAPIView.__name__)

    def test_genre_url(self):
        url = reverse('pages:genre', kwargs={'slug_genre': 'test_slug'})
        view = resolve(url)
        self.assertIs(view.func.view_class.__name__, views.FilterGenreAPIView.__name__)

    def test_film_commend_url(self):
        url = reverse('pages:add-commend', kwargs={'slug_film': 'test'})
        view = resolve(url)
        self.assertIs(view.func.view_class.__name__, views.CreateCommandAPIView.__name__)

    def test_film_answer_commend_url(self):
        url = reverse('pages:answer-commend', kwargs={'slug_film': 'test', 'pk_command': 1})
        view = resolve(url)
        self.assertIs(view.func.view_class.__name__, views.CreateAnswerCommandAPIView.__name__)
