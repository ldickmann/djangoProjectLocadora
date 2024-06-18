from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .forms import CadastroForm, LoginForm, VeiculoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Veiculo
from .utils import enviar_cadastro


# Criação das views, através de funções, responsáveis por renderizar as páginas html.

# A view index é a view principal, que retorna o modelo index.html.
def index(request):
    return render(request, 'index.html')


# A view login é responsável por autenticar o usuário.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('veiculos')
            else:
                messages.error(request, 'Acesso Negado. Verifique seu email e senha.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# A view cadastro é responsável por cadastrar um usuário.
def cadastro(request):
    if request.method == "POST":
        form = CadastroForm()
        return render(request, 'cadastro.html', {'form': form})
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password1']
            password_hash = make_password(password)

            # Cria o usuário no modelo User padrão
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=password_hash,
                is_active=False  # Define o usuário como inativo inicialmente
            )

            enviar_cadastro(user)  # Envia a notificação de aprovação

            messages.success(request, 'Cadastro enviado para aprovação. Aguarde nosso contato!')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados informados.')
        return render(request, 'cadastro.html', {'form': form})


# A view veiculos é responsável por listar os veículos cadastrados.
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    context = {'veiculos': veiculos}
    return render(request, 'veiculos.html', context)


# A view add_veiculo é responsável por cadastrar um veículo.
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


# A view edit_veiculo é responsável por editar um veículo.
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


# A view del_veiculo é responsável por excluir um veículo.
def del_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.delete()
        messages.success(request, 'Veículo excluído com sucesso!')
        return redirect('lista_veiculos')
    context = {'veiculo': veiculo}
    return render(request, 'del-veiculo.html', context)
