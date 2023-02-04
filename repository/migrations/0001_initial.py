# Generated by Django 4.1.6 on 2023-02-02 13:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('adventure', 'ماجراجویی'), ('romantic', 'عاشقانه'), ('drama', 'درام'), ('action', 'اکشن')], max_length=150)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
                ('imdb_rating', models.FloatField()),
                ('slug', models.SlugField(unique=True)),
                ('year_publication', models.DateField()),
                ('files', models.FileField(upload_to='')),
                ('play_status', models.CharField(choices=[('Finished', 'تمام شده'), ('Playing', 'در حال پخش')], max_length=50)),
                ('Quality', models.CharField(choices=[('480', '480'), ('720', '720'), ('1080', '1080')], max_length=50)),
                ('product', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=20)),
                ('period_time', models.TimeField()),
                ('description', ckeditor.fields.RichTextField()),
                ('genre', models.ManyToManyField(related_name='genre_serial', to='repository.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
                ('imdb_rating', models.FloatField()),
                ('slug', models.SlugField(unique=True)),
                ('year_publication', models.DateField()),
                ('file', models.FileField(upload_to='')),
                ('play_status', models.CharField(choices=[('Finished', 'تمام شده'), ('Playing', 'در حال پخش')], max_length=150)),
                ('Quality', models.CharField(choices=[('480', '480'), ('720', '720'), ('1080', '1080')], max_length=50)),
                ('product', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=20)),
                ('period_time', models.TimeField()),
                ('description', ckeditor.fields.RichTextField()),
                ('genre', models.ManyToManyField(related_name='genre_movie', to='repository.genre')),
            ],
        ),
    ]
