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

        # Verifica se o usuário já respondeu ao simulado
        respostas_usuario = Resposta.objects.filter(user=request.user, simulado_origem=simulado_desejado)

        # Passa as respostas do usuário para o template
        context = {
            'simulado': simulado_desejado, 
            'questoes': questoes,
            'respostas_usuario': respostas_usuario
        }

        return render(request, 'paginas/simulado.html', context)

    def post(self, request, idsimulado):
        simulado = Simulado.objects.get(id=idsimulado)
        user = request.user  # Captura o usuário autenticado

        for key, value in request.POST.items():
            if key.startswith("resposta_"):  # Identifica os inputs do formulário
                questao_id = key.split("_")[1]  # Obtém o ID da questão
                questao = Questao.objects.get(id=questao_id)

                # Verifica se o usuário já respondeu essa questão antes
                resposta_existente = Resposta.objects.filter(user=user, simulado_origem=simulado, questao=questao).first()

                if resposta_existente:
                    # Se já houver uma resposta, atualiza a resposta existente
                    resposta_existente.resposta = value
                    resposta_existente.save()
                else:
                    # Se não houver, cria uma nova resposta
                    Resposta.objects.create(
                        user=user,
                        simulado_origem=simulado,
                        questao=questao,
                        resposta=value
                    )

        return redirect('simulados')  # Redireciona para a lista de simulados após salvar

from django.http import JsonResponse # precisa disso pra enviar o json

class EditarView(View):
    def get(self, request, id): #esse id do argumento precisa ter o mesmo nome da url
        aulaselecionada= aulas.objects.get(id=id)
        context = {'aula': aulaselecionada}
        return render(request, "paginas/editaraula.html", context)
    
    def post(self, request, id):
        aulaselecionada= aulas.objects.get(id=id)
        nome = request.POST.get("nome")
        subtitulo = request.POST.get("subtitulo")
        aulaselecionada.nome = nome
        aulaselecionada.subtitulo = subtitulo
        aulaselecionada.save()
        #context = {'aula': aulaselecionada}

        return JsonResponse({
            "mensagem": "Aula atualizada com sucesso!",
            "nome": aulaselecionada.nome,
            "subtitulo": aulaselecionada.subtitulo
        })
    
        #return render(request,"paginas/editaraula.html", context)


        


