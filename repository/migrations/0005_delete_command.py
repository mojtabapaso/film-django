# Generated by Django 4.1.6 on 2023-02-07 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_film_remove_serial_genre_alter_command_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Command',
        ),
    ]
