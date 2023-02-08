from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.FilmAPIView.as_view()),
    path('detail/<str:slug_film>/', views.FilmDetailAPIView.as_view()),
    path('search/', views.FilmSearchAPIView.as_view()),
    path('filter/', views.FilterTypeAPIView.as_view()),
    path('genre/<str:slug_genre>/', views.FilterGenreAPIView.as_view()),
]
