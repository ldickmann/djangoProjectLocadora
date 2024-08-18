from RosaTrip.models import Veiculo
from RosaTrip.forms import VeiculoModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Criação das views, através de funções, responsáveis por renderizar as páginas html.


def home(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')


class VeiculosListView(ListView):
    model = Veiculo
    template_name = 'veiculos.html'
    context_object_name = 'veiculos'

    def get_queryset(self):
        veiculos = super().get_queryset().order_by('modelo')
        search = self.request.GET.get('search')
        if search:
            veiculos = veiculos.filter(modelo__icontains=search)
        return veiculos


class VeiculoDetailView(DetailView):
    model = Veiculo
    template_name = 'detalhe.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class VeiculoCreateView(CreateView):
    model = Veiculo
    form_class = VeiculoModelForm
    template_name = 'add-veiculo.html'
    success_url = '/veiculos/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class VeiculoUpdateView(UpdateView):
    model = Veiculo
    form_class = VeiculoModelForm
    template_name = 'edit-veiculo.html'

    def get_success_url(self):
        return reverse_lazy('detalhe', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = 'del-veiculo.html'
    success_url = '/veiculos/'
