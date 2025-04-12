from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

def colaborador(request):
    return render(request, "colaborador.html")