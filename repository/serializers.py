from rest_framework import serializers
from .models import Genre, Film


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
