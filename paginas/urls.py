from django.urls import path
from .views import SimuladosView
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastraraulas', views.cadastrar_aula, name="cadastraraulas"),
    path('apagaraula/<str:idaula>/', views.apagar_aula, name="apagaraula"),
    path('simulados/', SimuladosView.as_view(), name="simulados"),
    path('simulados/<int:idsimulado>/', SimuladoView.as_view(), name="simulado_especifico"),
    path('editaraula/<int:id>/', EditarView.as_view(), name="editaraula"),
    path('login/', LoginView.as_view(), name="login"),
    path('cadastro/', CadastroView.as_view(), name="cadastro"),
    path('verteste', SimuladoTestee.as_view(), name='verteste'),
]