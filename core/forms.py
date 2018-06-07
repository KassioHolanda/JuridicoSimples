from django import forms
from django.contrib.auth import get_user_model
from django.forms.widgets import ClearableFileInput

from core.models import User, Postagem, Theme

User = get_user_model()


class RegisterUser(forms.ModelForm):
    senha1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Confirmacao de Senha', widget=forms.PasswordInput)

    def verificar_senha(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError("A Confirmacao nao esta Correta")
        return senha2

    def save(self, commit=True):
        user = super(RegisterUser, self).save(commit=False)
        user.set_password(self.cleaned_data['senha1'])

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        # abstract = True
        fields = ['username', 'email']


class RegiterNewsForm(forms.ModelForm):
    # Titulo = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
    #                        required=False)
    # Resumo = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'materialize-textarea'}),
    #                        required=False)
    # image = forms.ImageField(widget=ClearableFileInput)
    # body = forms.CharField(label='Corpo da Noticia', max_length=255,
    #                        widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),
    #                        required=False)

    class Meta:
        model = Postagem
        fields = '__all__'
        widgets = {
            'Titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Titulo da Postagem'
            }),
            # 'resumo'
        }

        error_messages = {
            'Titulo': {
                'required': 'O campo nome é obrigatório'
            },
            # 'resume'
        }


class RegistrarTemaFormulario(forms.ModelForm):
    class Meta:
        model = Theme
        fields = '__all__'
