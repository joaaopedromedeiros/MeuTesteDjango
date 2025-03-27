from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(aulas)
admin.site.register(Simulado)
admin.site.register(Questao)
admin.site.register(Resposta)
admin.site.register(SimuladoTeste)
admin.site.register(QuestaoSimulado)
admin.site.register(TextoSimulado)
admin.site.register(QuestaoSimuladoAlternativa)
