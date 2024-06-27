from django import forms
from . models import Veiculo


# Classe de formulário de veículo
class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


# Classe de formulário de login
class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome de Usuário",
                "class": "form-control form-input"
            }
        ))

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-input"
            }
        ))


# Classe de formulário de cadastro
class CadastroForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome de Usuário",
                "class": "form-control form-input"
            }
        ))
    first_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome",
                "class": "form-control form-input"
            }
        ))
    last_name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sobrenome",
                "class": "form-control form-input"
            }
        ))
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control form-input"
            }
        ))
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control form-input"
            }
        ))
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirme sua Senha",
                "class": "form-control form-input"
            }
        ))

    # Método/Função de validação de senha
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas não conferem')

        return cleaned_data