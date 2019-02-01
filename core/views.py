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


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoa')
    else:
        return render(request, 'core/update_pessoa.html', data)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoa')
    else:
        return render(request, 'core/delete_confirm.html', {'pessoa': pessoa})


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


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculo')
    else:
        return render(request, 'core/update_veiculo.html', data)


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


def movrotativos_update(request, id):
    data = {}
    mov_rotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov_rotativo)
    data['mov_rotativo'] = mov_rotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_mov_rot.html', data)


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


def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)


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


def movmensalista_update(request, id):
    data = {}
    movmensalista = MovMensalista.objects.get(id=id)
    form = MovmensalistaForm(request.POST or None, instance=movmensalista)
    data['movmensalista'] = movmensalista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_mensalistas')
    else:
        return render(request, 'core/update_movmensalista.html', data)
