# Generated by Django 4.1.6 on 2023-02-08 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_remove_command_film_command_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='sub_command',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.command'),
        ),
    ]