# Generated by Django 4.1.6 on 2023-02-07 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_delete_command'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='Quality',
            field=models.CharField(choices=[('360', '360'), ('480', '480'), ('720', '720'), ('1080', '1080')], max_length=50),
        ),
        migrations.AlterField(
            model_name='film',
            name='type',
            field=models.CharField(choices=[('movie', 'فیلم'), ('serial', 'سریال')], max_length=50),
        ),
    ]
