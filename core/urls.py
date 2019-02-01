from django.urls import path, include, re_path
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
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
    veiculo_update
)

urlpatterns = [
    path('', home, name='core_home'),

    path('pessoas/', lista_pessoas, name='core_lista_pessoa'),
    path('pessoa-novo/', pessoa_novo, name='core_pessoa_novo'),
    re_path('pessoa-update(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),

    
    path('veiculos/', lista_veiculos, name='core_lista_veiculo'),
    path('veiculo-novo/', veiculo_novo, name='core_veiculo_novo'),
    re_path('veiculo-update(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),

    
    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mov-rot-novo/', movrotativos_novo, name='core_movrotativos_novo'),
    
    path('mensalistas/', lista_mensalista, name='core_lista_mensalista'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),
    
    path('mov-mensalistas/', lista_mov_mensalistas, name='core_lista_mov_mensalistas'),
    path('mov-mensalista-novo/', movmensalista_novo, name='core_movmensalista_novo'),
]
