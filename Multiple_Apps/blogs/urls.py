from django.urls import path
from . import views
urlpatterns = [
    path('',views.root),
    path('blogs/', views.index),       # would match localhost:8000/bears/23
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy),
    path('blogs/json', views.json),
]