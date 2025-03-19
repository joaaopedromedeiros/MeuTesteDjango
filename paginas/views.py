from django.shortcuts import render, redirect
from .models import aulas
# Create your views here.

def home(request):
    aulass = aulas.objects.all()
    return render(request, "paginas/home.html", {'aulas': aulass})

def cadastrar_aula(request):
    if request.method == 'POST':
        nome = request.POST.get('aula')
        subtitulo = request.POST.get('subtitulo')
        aulas.objects.create(nome=nome, subtitulo=subtitulo)
        return redirect('home')
        
    return render(request, 'paginas/home.html')  # Exibe o formulário para a primeira vez


def apagar_aula(request, idaula):
    objeto = aulas.objects.get(id=idaula)
    objeto.delete()
    return redirect('home')

