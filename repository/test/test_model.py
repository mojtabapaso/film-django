from django.test import TestCase
from ..models import Film, Genre


class TestFilm(TestCase):
    def setUp(self):
        genre = Genre.objects.create(name='test', slug='test')
        self.film = Film.objects.create(name='test name film', year_publication='2020-12-12', play_status='published',
                                        Quality='720', product='Iran', language='Parsi', period_time=50.2,
                                        description='test text', is_movie=True, is_serial=False)
        self.film.genre.set([genre])

    def test__value_equal_in_instance_model_film(self):
        film = Film.objects.get(id=1)
        self.assertEqual(self.film.genre, film.genre)
        self.assertEqual(self.film.name, film.name)
        self.assertEqual(self.film.slug, film.slug)
        self.assertEqual(self.film.year_publication, str(film.year_publication))
        self.assertEqual(self.film.play_status, film.play_status)
        self.assertEqual(self.film.Quality, film.Quality)
        self.assertEqual(self.film.product, film.product)
        self.assertEqual(self.film.language, film.language)
        self.assertEqual(self.film.period_time, film.period_time)
        self.assertEqual(self.film.description, film.description)
        self.assertEqual(self.film.is_movie, film.is_movie)
        self.assertEqual(self.film.is_serial, film.is_serial)

    def test_value_in_model(self):
        film = Film.objects.get(id=1)
        self.assertTrue(film.is_movie)
        self.assertFalse(film.is_serial)
        self.assertEqual(film.product, 'Iran')
        self.assertEqual(film.name, 'test name film')
        self.assertEqual(str(film.year_publication), '2020-12-12')
        self.assertEqual(film.play_status, 'published')
        self.assertEqual(film.Quality, '720')
        self.assertEqual(film.language, 'Parsi')
        self.assertEqual(film.period_time, 50.2)
        self.assertEqual(film.description, 'test text')

    def test_str(self):
        self.assertEqual(str(self.film), self.film.name)


class TestGenre(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name='test', slug='test')

    def test_equal_value_in_instance(self):
        genre = Genre.objects.get(id=1)
        self.assertEqual(self.genre.name, genre.name)
        self.assertEqual(self.genre.slug, genre.slug)

    def test_value_in_model(self):
        self.assertEqual(self.genre.name, 'test')
        self.assertEqual(self.genre.slug, 'test')
