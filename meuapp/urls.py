from django.urls import path
from meuapp import views

urlpatterns = [
     path('', views.home),
     path('menu/', views.menu),
     path('colaborador/', views.colaborador, name= "colaborador"),
     path('cadastrar/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
]