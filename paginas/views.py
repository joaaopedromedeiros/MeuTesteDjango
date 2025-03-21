from django.shortcuts import render, redirect
from django.views import View
from .models import aulas
from .models import *
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


class SimuladosView(View):
    def get(self, request):
        simulados = Simulado.objects.all()
        context = {'simulados': simulados}
        return render(request, "paginas/simulados.html", context)
    
    def post(self, request):
        pass


class SimuladoView(View):
    def get(self, request, idsimulado):
        simulado_desejado = Simulado.objects.get(id=idsimulado)
        
        questoes = Questao.objects.filter(simulado=simulado_desejado)
        context = {'simulado': simulado_desejado, 'questoes': questoes}


        return render(request,'paginas/simulado.html', context)


