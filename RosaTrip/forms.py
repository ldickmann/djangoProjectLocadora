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
        label='Nome de Usuário',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome de Usuário",
                "class": "form-control"
            }
        ))

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


# Classe de formulário de cadastro
class CadastroForm(forms.Form):
    username = forms.CharField(
        label='Nome de Usuário',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome de Usuário",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        label='Nome',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        label='Sobrenome',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Sobrenome",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        label='Confirmação de Senha',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirme sua Senha",
                "class": "form-control"
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