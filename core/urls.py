from django.urls import path, include
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movrotativos, 
    lista_mensalista,
    lista_mov_mensalistas,
    pessoa_novo,
    veiculo_novo,
    movrotativos_novo,
    mensalista_novo
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoa'),
    path('pessoa-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('veiculo-novo/', veiculo_novo, name='core_veiculo_novo'),
    path('mov-rot-novo/', movrotativos_novo, name='core_movrotativos_novo'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculo'),
    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mensalistas/', lista_mensalista, name='core_lista_mensalista'),
    path('mov-mensalistas/', lista_mov_mensalistas, name='core_lista_mov_mensalistas'),
]
