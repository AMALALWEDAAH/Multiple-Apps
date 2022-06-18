from django.urls import path
from . import views
urlpatterns = [
    path('/surveys', views.surveys),       # would match localhost:8000/bears/23
    path('/surveys/new', views.new),
]