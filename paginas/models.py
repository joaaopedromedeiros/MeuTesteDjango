from django.db import models

# Create your models here.

class aulas(models.Model):
    id = models.AutoField(primary_key=True)
    subtitulo = models.CharField(max_length=200, default="Subtitulo")
    nome = models.CharField(max_length=200)

    def __str__(self):
        return f'Aula: {self.nome}, Subtítulo: {self.subtitulo}'




