from django.urls import path
from meuapp import views

urlpatterns = [
     path('', views.home),
]