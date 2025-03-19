from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastraraulas', views.cadastrar_aula, name="cadastraraulas"),
    path('apagaraula/<str:idaula>/', views.apagar_aula, name="apagaraula")
]