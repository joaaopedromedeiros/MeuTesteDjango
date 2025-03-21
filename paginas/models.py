from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class aulas(models.Model):
    id = models.AutoField(primary_key=True)
    subtitulo = models.CharField(max_length=200, default="Subtitulo")
    nome = models.CharField(max_length=200)

    def __str__(self):
        return f'Aula: {self.nome}, Subtítulo: {self.subtitulo}'


# models simulados






class Simulado(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ano = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.nome}  {self.ano}'



class Questao(models.Model):
    id = models.AutoField(primary_key=True)
    simulado = models.ForeignKey(Simulado, on_delete=models.CASCADE )
    numero_questao = models.CharField(max_length=2, default=1)
    enunciado = models.CharField(max_length=1000)
    alternativa_a = models.CharField(max_length=100)
    alternativa_b = models.CharField(max_length=100)
    alternativa_c = models.CharField(max_length=100)
    alternativa_d = models.CharField(max_length=100)

    def __str__(self):
        return f'QuestãoDoSimulado: {self.simulado}, NúmeroQuestão: {self.numero_questao} '

class Resposta(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    simulado_origem = models.ForeignKey(Simulado, on_delete=models.CASCADE, default=1)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE, default=1)
    resposta = models.CharField(max_length=200, default=1)

    def __str__(self):
        return f'Usuario: {self.user}, Simulado: {self.simulado_origem}, Questão: {self.questao}, Resposta: {self.resposta} '




