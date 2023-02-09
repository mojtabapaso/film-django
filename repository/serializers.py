from rest_framework import serializers

from .custom_relational_fields import GenreShowRelational
from .models import Genre, Film


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class FilmSerializers(serializers.ModelSerializer):
    genre = GenreShowRelational(read_only=True)

    class Meta:
        model = Film
        fields = '__all__'
