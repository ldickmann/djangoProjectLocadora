from RosaTrip.models import Veiculo
from RosaTrip.forms import VeiculoModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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


@method_decorator(login_required(login_url='login'), name='dispatch')
class VeiculoCreateView(CreateView):
    model = Veiculo
    form_class = VeiculoModelForm
    template_name = 'add-veiculo.html'
    success_url = '/veiculos/'
