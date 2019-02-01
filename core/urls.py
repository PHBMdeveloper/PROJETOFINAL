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
    veiculo_update,
    movrotativos_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    movrotativos_delete,
    mensalista_delete,
    movmensalista_delete
)

urlpatterns = [
    path('', home, name='core_home'),

    path('pessoas/', lista_pessoas,
         name='core_lista_pessoa'),
    path('pessoa-novo/', pessoa_novo,
         name='core_pessoa_novo'),
    re_path(r'pessoa-update/(?P<id>\d+)/$', pessoa_update,
            name='core_pessoa_update'),
    re_path(r'pessoa-delete/(?P<id>\d+)/$', pessoa_delete,
            name='core_pessoa_delete'),

    path('veiculos/', lista_veiculos,
         name='core_lista_veiculo'),
    path('veiculo-novo/', veiculo_novo,
         name='core_veiculo_novo'),
    re_path(r'veiculo-update/(?P<id>\d+)/$', veiculo_update,
            name='core_veiculo_update'),
    re_path(r'veiculo-delete/(?P<id>\d+)/$', veiculo_delete,
            name='core_veiculo_delete'),

    path('mov-rot/', lista_movrotativos,
         name='core_lista_movrotativos'),
    path('mov-rot-novo/', movrotativos_novo,
         name='core_movrotativos_novo'),
    re_path(r'mov-rot-update/(?P<id>\d+)/$', movrotativos_update,
            name='core_movrotativos_update'),
    re_path(r'mov-rot-delete/(?P<id>\d+)/$', movrotativos_delete,
            name='core_movrotativos_delete'),

    path('mensalistas/', lista_mensalista,
         name='core_lista_mensalista'),
    path('mensalista-novo/', mensalista_novo,
         name='core_mensalista_novo'),
    re_path(r'mensalista-update/(?P<id>\d+)/$', mensalista_update,
            name='core_mensalista_update'),
    re_path(r'mensalista-delete/(?P<id>\d+)/$', mensalista_delete,
            name='core_mensalista_delete'),

    path('mov-mensal/', lista_mov_mensalistas,
         name='core_lista_mov_mensalistas'),
    path('mov-mensal-novo/', movmensalista_novo,
         name='core_movmensalista_novo'),
    re_path(r'mov-mensal-update/(?P<id>\d+)/$', movmensalista_update,
            name='core_movmensalista_update'),
    re_path(r'mov-mensal-delete/(?P<id>\d+)/$', movmensalista_delete,
            name='core_movmensalista_delete'),
]
