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


class SimuladoTeste(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    duracao = models.CharField(max_length=1) 
    

    def __str__(self):
        return f'{self.id} - {self.nome} ({self.duracao})'

class QuestaoSimulado(models.Model):
    id = models.AutoField(primary_key=True)
    id_simulado = models.ForeignKey(SimuladoTeste, on_delete=models.CASCADE, related_name="questoes" )
    numero_questao = models.CharField(max_length=2) # Adiconei, não estava no diagrama
    enunciado = models.CharField(max_length=10000)
    imagem = models.ImageField(upload_to='images/',blank=True, null=True) # para aonde fazer upload?

    def __str__(self):
        return f'Questão: {self.numero_questao} do Simulado: {self.id_simulado.nome}'
    
class TextoSimulado(models.Model):
    id = models.AutoField(primary_key=True)
    id_simulado = models.ForeignKey(SimuladoTeste, on_delete=models.CASCADE, related_name="textos" )
    titulo = models.CharField(max_length=100)
    conteudo = models.CharField(max_length=100000)
    referencia = models.CharField(max_length=1000)
    imagem = models.ImageField(upload_to='images/',blank=True, null=True) # para aonde fazer upload?

    def __str__(self):
        return f'Texto {self.titulo} do simulado {self.id_simulado.nome}'


class QuestaoSimuladoAlternativa(models.Model):
    id = models.AutoField(primary_key=True)
    id_questao = models.ForeignKey(QuestaoSimulado, on_delete=models.CASCADE, related_name="alternativas"  )
    correta = models.BooleanField(default=False)
    texto = models.CharField(max_length=10000)
    sla = models.CharField(max_length=1, default=1)

    def __str__(self):
        return f'Alternativa da questão {self.id_questao.numero_questao}, simulado {self.id_questao.id_simulado.nome}'




