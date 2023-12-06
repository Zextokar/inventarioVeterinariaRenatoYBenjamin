from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioFormRegistration(UserCreationForm):
    username = forms.CharField(max_length=99, required=True)
    password1 = forms.CharField(max_length=99, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=99, required=True, widget=forms.PasswordInput)
    is_staff = forms.BooleanField(required=False,initial=False)
    is_superuser = forms.BooleanField(required=False,initial=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_staff', 'is_superuser']

    username.widget.attrs['class'] = 'form-control'
    password1.widget.attrs['class'] = 'form-control'
    password2.widget.attrs['class'] = 'form-control'
    is_staff.widget.attrs['class'] = 'form-input'
    is_superuser.widget.attrs['class'] = 'form-input'