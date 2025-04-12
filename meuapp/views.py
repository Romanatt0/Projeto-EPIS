from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Colaborador  # Supondo que você criou esse model

def cadastrar_colaborador(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')

        if nome and cargo:
            Colaborador.objects.create(nome=nome, cargo=cargo)
            return render(request, 'cadastro.html', {'sucesso': True})

    return render(request, 'cadastro.html')

def home(request):
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

def colaborador(request):
    return render(request, "colaborador.html")

def listar_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'listar.html', {'colaboradores': colaboradores})
