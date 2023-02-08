from rest_framework import generics
from repository.models import Film, Genre
from repository.serializers import FilmSerializers
from rest_framework import filters


class FilmAPIView(generics.ListAPIView):
    """
    return all film and serial in database
    """
    serializer_class = FilmSerializers
    queryset = Film.objects.all()


class FilmDetailAPIView(generics.ListAPIView):
    """
    show detail film or serial
    """
    serializer_class = FilmSerializers

    def get_queryset(self):
        slug = self.kwargs['slug_film']
        return Film.objects.filter(slug=slug)


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
