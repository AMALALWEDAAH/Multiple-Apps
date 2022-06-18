from django.urls import path
from . import views
urlpatterns = [
    path('/register', views.register),       # would match localhost:8000/bears/23
    path('/login', views.login),
    path('/users/new', views.register),
    path('/users', views.users),
]