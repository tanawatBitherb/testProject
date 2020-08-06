from django.urls import path, include
from . import views

app_name = 'reservation'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('homepage/', views.homepage, name='homepage'),

]