from django import forms
from principal.models import livros
from django.contrib.auth.forms import AuthenticationForm

class livroform(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-label form-control'}))
    editora = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-label form-control'}))
    preco = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-label form-control'}))
    class Meta:
        model = livros
        fields = ["titulo", "editora", "preco"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-floating form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-floating form-control'}))