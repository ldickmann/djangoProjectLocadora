from django import forms
from RosaTrip.models import Veiculo


class VeiculoModelForm(forms.ModelForm):

    class Meta:
        model = Veiculo
        fields = '__all__'
