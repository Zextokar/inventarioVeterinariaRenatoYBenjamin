from dataclasses import fields
from django import forms
from django.urls import include
from gestorProducts.models import *
from django.core import validators

class ProductoFormRegistration(forms.Form):
    codigo = forms.IntegerField(
        validators=[
            validators.MinValueValidator(1),
        ]
    )
    nombre = forms.CharField(
        validators=[
            validators.MinLengthValidator(1),
            validators.MaxLengthValidator(99),
        ]
    )
    descripcion = forms.CharField(max_length=99)
    precio = forms.IntegerField()
    categoria = forms.ModelChoiceField(queryset=Categorias.objects.all())

    codigo.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'

class ProductoFormRegistration(forms.ModelForm):
    codigo = forms.IntegerField(
        validators=[
            validators.MinValueValidator(1),
        ]
    )
    nombre = forms.CharField(
        validators=[
            validators.MinLengthValidator(1),
            validators.MaxLengthValidator(99),
        ]
    )
    descripcion = forms.CharField(max_length=99)
    precio = forms.IntegerField()
    categoria = forms.ModelChoiceField(queryset=Categorias.objects.all())

    codigo.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Producto
        exclude = ['user']

class CategoriaFormRegistration(forms.Form):
    codigo = forms.IntegerField(
        validators=[
            validators.MinValueValidator(1),
        ]
    )
    nombre = forms.CharField(
        validators=[
            validators.MinLengthValidator(1),
            validators.MaxLengthValidator(99),
        ]
    )

    codigo.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['class'] = 'form-control'
class CategoriaFormRegistration(forms.ModelForm):
    codigo = forms.IntegerField(
        validators=[
            validators.MinValueValidator(1),
        ]
    )
    nombre = forms.CharField(
        validators=[
            validators.MinLengthValidator(1),
            validators.MaxLengthValidator(99),
        ]
    )

    codigo.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Categorias
        fields = '__all__'
