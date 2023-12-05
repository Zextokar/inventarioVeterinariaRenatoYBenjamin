from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from gestorUser.forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def Dashboard(request):
    return render(request, 'veterinariaChucky/dashboard.html')

# Vista Usuarios
@login_required
def Usergestion(request):
    producto = User.objects.all()
    data = {
        'productos' : producto,
    }
    return render(request, 'veterinariaChucky/usergestion.html', data)

@login_required
def InsertUser(request):
    if request.method == 'POST':
        form = UsuarioFormRegistration(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('usergestion'))

    else:
        form = UsuarioFormRegistration()

    data = {
        'form': form,
        'title': 'Registrar Usuario'
    }

    return render(request, 'veterinariaChucky/insertUser.html', data)

@login_required
def editUser(request, id):
    categorias = User.objects.get(id=id)
    form = UsuarioFormRegistration(instance=categorias)
    if request.method == 'POST':
        form = UsuarioFormRegistration(request.POST, instance=categorias)
        if form.is_valid():
            print("El form es valido")
            form.save()
            return HttpResponseRedirect(reverse('usergestion'))
        else:
            print("Hay errores: ", form.errors)
    data = {
        'form': form,
        'title': 'Editar Usuarios'
    }
    return render(request, 'veterinariaChucky/insertUser.html', data)

@login_required
def deleteUser(request, id):
    if request.user.is_superuser:
        producto = User.objects.get(id = id)
        producto.delete()
        return HttpResponseRedirect(reverse('usergestion'))
    else:
        return render(request, 'veterinariaChucky/dashboard.html')