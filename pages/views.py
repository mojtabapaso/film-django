from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from pages.serializers import CommandSerializers, CreateCommandSerializers, CreateAnswerCommandSerializers
from repository.models import Film, Genre
from repository.serializers import FilmSerializers
from rest_framework import filters
# generics.ListCreateAPIView
from .models import Command
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class FilmAPIView(generics.ListAPIView):
    """
    return all film and serial in database
    """
    serializer_class = FilmSerializers
    queryset = Film.objects.all()


class FilmDetailAPIView(APIView):
    """
    show detail page film or serial
    """
    serializer_class = FilmSerializers, CommandSerializers

    def get(self, request, slug_film):
        film = get_object_or_404(Film, slug=slug_film)
        command = film.command.all()
        ser_data = FilmSerializers(instance=film).data
        ser_data_command = CommandSerializers(instance=command, many=True).data
        return Response([ser_data, ser_data_command], status=status.HTTP_200_OK)


class CreateCommandAPIView(APIView):
    """
    create command for film with slug film
    by default active is False and in admin panel after see can change them

    """
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCommandSerializers

    def post(self, request, slug_film):
        film = get_object_or_404(Film, slug=slug_film)
        ser_data = CreateCommandSerializers(data=request.POST)
        if ser_data.is_valid():
            vd = ser_data.validated_data

            ser_data.validated_data['user'] = request.user
            Command.objects.create(user=request.user, film=film, text=vd['text'], score=vd['score'])

            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateAnswerCommandAPIView(APIView):
    """
    create answer for command with slug film and id command
    """

    permission_classes = [IsAuthenticated]
    serializer_class = CreateAnswerCommandSerializers

    def post(self, request, slug_film, pk_command):
        film = get_object_or_404(Film, slug=slug_film)
        command = get_object_or_404(Command, pk=pk_command)
        ser_data = CreateAnswerCommandSerializers(data=request.POST)
        if ser_data.is_valid():
            ser_data.validated_data['user'] = request.user
            Command.objects.create(user=request.user, film=film, sub_command=command, is_sub_command=True,
                                   text=ser_data.validated_data['text'])

            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmSearchAPIView(generics.ListAPIView):
    """
     search  in name and description and name of genre film

    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'genre__name']


class FilterTypeAPIView(generics.ListAPIView):
    """ filter by is serial or is movie if send both them ,send all query  """
    queryset = Film.objects.all()
    serializer_class = FilmSerializers

    def get_queryset(self):
        queryset = Film.objects.all()
        is_serial = self.request.query_params.get('serial')
        is_movie = self.request.query_params.get('movie')
        if is_serial and is_movie:
            return queryset
        if is_serial:
            queryset = queryset.filter(is_serial=is_serial)
            return queryset
        if is_movie:
            queryset = queryset.filter(is_movie=is_movie)
            return queryset
        return queryset


class FilterGenreAPIView(generics.ListAPIView):
    """
    filter by genre film or serial
    """
    serializer_class = FilmSerializers

    def get_queryset(self):
        slug = self.kwargs['slug_genre']
        genre = Genre.objects.get(slug=slug)
        return Film.objects.filter(genre=genre)
