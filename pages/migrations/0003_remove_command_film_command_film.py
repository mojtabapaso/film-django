# Generated by Django 4.1.6 on 2023-02-07 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_delete_command'),
        ('pages', '0002_command_delete_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='film',
        ),
        migrations.AddField(
            model_name='command',
            name='film',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='command', to='repository.film'),
        ),
    ]