from django.contrib.auth.hashers import make_password
from .forms import CadastroForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Veiculo, CadastroPendente
from .forms import VeiculoForm
from .utils import enviar_cadastro


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('senha')

        user = authenticate(username=email, password=password)

        if user:
            auth_login(request, user)
            return redirect('veiculos')
        else:
            messages.error(request, 'Acesso Negado. Verifique seu email e senha.')
            return redirect('login')


def cadastro(request):
    if request.method == "GET":
        form = CadastroForm()
        return render(request, 'cadastro.html', {'form': form})
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password1']
            password_hash = make_password(password)
            cadastro_pendente = CadastroPendente.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=password_hash
            )

            enviar_cadastro(cadastro_pendente)

            messages.success(request, 'Dados cadastrados enviados com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados informados.')
        return render(request, 'cadastro.html', {'form': form})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    context = {'veiculos': veiculos}
    return render(request, 'veiculos.html', context)


def add_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo cadastrado com sucesso!')
            return redirect('lista_veiculos')
    else:
        form = VeiculoForm()
    context = {'form': form}
    return render(request, 'add-veiculo.html', context)


def edit_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo editado com sucesso!')
            return redirect('lista_veiculos')
    else:
        form = VeiculoForm(instance=veiculo)
    context = {'form': form}
    return render(request, 'edit-veiculo.html', context)


def del_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.delete()
        messages.success(request, 'Veículo excluído com sucesso!')
        return redirect('lista_veiculos')
    context = {'veiculo': veiculo}
    return render(request, 'del-veiculo.html', context)
