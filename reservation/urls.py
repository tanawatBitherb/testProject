from django.urls import path, include
from reservation import views, login

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login.login, name='login'),
    path('register/', views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
]