from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
type_genre = (
    ('ماجراجویی', 'ماجراجویی'), ('عاشقانه', 'عاشقانه'), ('درام', 'درام'), ('اکشن', 'اکشن'), ('مستند', 'مستند'))
status = (('Finished', 'تمام شده'), ('Playing', 'در حال پخش'))
quality = (('360', '360'), ('480', '480'), ('720', '720'), ('1080', '1080'))


class Genre(models.Model):
    name = models.CharField(choices=type_genre, max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True)
    year_publication = models.DateField()
    file = models.FileField(null=True, blank=True)
    play_status = models.CharField(choices=status, max_length=150)
    Quality = models.CharField(choices=quality, max_length=50)
    product = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre, related_name='genre_movie')
    language = models.CharField(max_length=20)
    period_time = models.FloatField()
    description = RichTextField()
    is_movie = models.BooleanField(null=True, blank=True)
    is_serial = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name
