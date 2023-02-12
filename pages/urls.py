from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.FilmAPIView.as_view(), name='home'),
    path('detail/<str:slug_film>/', views.FilmDetailAPIView.as_view(), name='detail'),
    path('search/', views.FilmSearchAPIView.as_view(), name='search'),
    path('filter/', views.FilterTypeAPIView.as_view(), name='filter'),
    path('genre/<str:slug_genre>/', views.FilterGenreAPIView.as_view(), name='genre'),
    path('add/command/<str:slug_film>/', views.CreateCommandAPIView.as_view(), name='add-commend'),
    path('add/command/<str:slug_film>/<int:pk_command>/', views.CreateAnswerCommandAPIView.as_view(),
         name='answer-commend'),
]
