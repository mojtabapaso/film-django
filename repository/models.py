from ckeditor.fields import RichTextField
from django.db import models

type_genre = (('adventure', 'ماجراجویی'), ('romantic', 'عاشقانه'), ('drama', 'درام'), ('action', 'اکشن'))


class Genre(models.Model):
    name = models.CharField(choices=type_genre, max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


status = (('Finished', 'تمام شده'), ('Playing', 'در حال پخش'))
quality = (('480', '480'), ('720', '720'), ('1080', '1080'))


class Movie(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    imdb_rating = models.FloatField()
    slug = models.SlugField(unique=True)
    year_publication = models.DateField()
    file = models.FileField()
    play_status = models.CharField(choices=status, max_length=150)
    Quality = models.CharField(choices=quality, max_length=50)
    product = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre, related_name='genre_movie')
    language = models.CharField(max_length=20)
    period_time = models.FloatField()
    description = RichTextField()

    def __str__(self):
        return self.name


class Serial(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    imdb_rating = models.FloatField()
    slug = models.SlugField(unique=True)
    year_publication = models.DateField()
    files = models.FileField()
    play_status = models.CharField(choices=status, max_length=50)
    Quality = models.CharField(choices=quality, max_length=50)
    product = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre, related_name='genre_serial')
    language = models.CharField(max_length=20)
    period_time = models.FloatField()
    description = RichTextField()

    def __str__(self):
        return self.name
