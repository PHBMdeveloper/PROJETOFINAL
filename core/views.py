from django.shortcuts import render, redirect
from .models import (
    Pessoa, 
    Veiculo, 
    MovRotativo,
    Mensalista, 
    MovMensalista
)

from .form import (
        PessoaForm, 
        VeiculoForm, 
        MovRotativoForm, 
        MensalistaForm,
        MovmensalistaForm
)


def home(request):
    context = {'mensagem': 'Ola mundo'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
        form = PessoaForm(request.POST or None)
        if form.is_valid():
                form.save()
        return redirect('core_lista_pessoa')

def lista_veiculos(request):
        form = VeiculoForm()
        veiculos = Veiculo.objects.all
        data = {'veiculos': veiculos, 'form': form}
        return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
        form = VeiculoForm(request.POST or None)
        if form.is_valid():
                form.save()
        return redirect('core_lista_veiculo')

def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all
    form = MovRotativoForm()
    data = {'mov_rot': mov_rot, 'form': form}
    return render(request, 'core/lista_mov_rot.html', data)


def movrotativos_novo(request):
        form = MovRotativoForm(request.POST or None)
        if form.is_valid():
                form.save()
        return redirect('core_lista_movrotativos')


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)


def mensalista_novo(request):
        form = MensalistaForm(request.POST or None)
        if form.is_valid():
                form.save()
        return redirect('core_lista_mensalista')


def lista_mov_mensalistas(request):
    mov_mensalistas = MovMensalista.objects.all
    form = MovmensalistaForm()
    data = {'mov_mensalistas': mov_mensalistas, 'form': form}
    return render(request, 'core/lista_mov_mensalistas.html', data)


def movmensalista_novo(request):
        form = MovmensalistaForm(request.POST or None)
        if form.is_valid():
                form.save()
        return redirect('core_lista_mov_mensalistas')
        
