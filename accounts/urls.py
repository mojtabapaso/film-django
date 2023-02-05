from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
    path('profile/', views.ProfileShowAPIView.as_view()),
    path('update/profile/<int:pk>/', views.ProfileUpdateAPIView.as_view()),

]
