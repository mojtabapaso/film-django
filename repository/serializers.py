from rest_framework import serializers
from .models import Genre, Serial, Movie


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class SerialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = '__all__'


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
