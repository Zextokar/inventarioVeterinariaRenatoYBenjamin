from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from gestorProducts.models import *
from gestorProducts.forms import *

# Create your views here.

# Vista de Productos
@login_required
def Productos(request):
    producto = Producto.objects.all()
    data = {
        'productos' : producto,
    }
    return render(request, 'veterinariaChucky/producto.html', data)
@login_required
def insertProductos(request):
    if request.method == 'POST':
        form = ProductoFormRegistration(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('productos'))

    else:
        form = ProductoFormRegistration()

    data = {
        'form': form,
        'title': 'Registrar Producto'
    }

    return render(request, 'veterinariaChucky/insertComponents.html', data)

@login_required
def editarProductos(request, id):
    producto = Producto.objects.get(id=id)
    form = ProductoFormRegistration(instance=producto)
    if request.method == 'POST':
        form = ProductoFormRegistration(request.POST, instance=producto)
        if form.is_valid():
            print("El form es valido")
            form.save()
            return HttpResponseRedirect(reverse('productos'))
        else:
            print("Hay errores: ", form.errors)
    data = {
        'form': form,
        'title': 'Editar Productos'
    }
    return render(request, 'veterinariaChucky/insertComponents.html', data)
@login_required
def eliminarProductos(request, id):
    if request.user.is_superuser:
        producto = Producto.objects.get(id = id)
        producto.delete()
        return HttpResponseRedirect(reverse('productos'))
    else:
        return render(request, 'veterinariaChucky/dashboard.html')
    
# Vista de Categorias:

@login_required
def Categoria(request):
    if request.user.is_superuser:
        producto = Categorias.objects.all()
        data = {
            'productos' : producto,
        }
        return render(request, 'veterinariaChucky/categoria.html', data)
    else:
        return render(request, 'veterinariaChucky/dashboard.html')
    
@login_required
def insertCategorias(request):
    if request.method == 'POST':
        form = CategoriaFormRegistration(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('categorias'))

    else:
        form = CategoriaFormRegistration()

    data = {
        'form': form,
        'title': 'Registrar Categoria'
    }

    return render(request, 'veterinariaChucky/insertComponents.html', data)
    
@login_required
def editarCategoria(request, id):
    categorias = Categorias.objects.get(id=id)
    form = CategoriaFormRegistration(instance=categorias)
    if request.method == 'POST':
        form = CategoriaFormRegistration(request.POST, instance=categorias)
        if form.is_valid():
            print("El form es valido")
            form.save()
            return HttpResponseRedirect(reverse('categorias'))
        else:
            print("Hay errores: ", form.errors)
    data = {
        'form': form,
        'title': 'Editar Categoria'
    }
    return render(request, 'veterinariaChucky/insertComponents.html', data)

@login_required
def eliminarCategoria(request, id):
    if request.user.is_superuser:
        producto = Categorias.objects.get(id = id)
        producto.delete()
        return HttpResponseRedirect(reverse('categorias'))
    else:
        return render(request, 'veterinariaChucky/dashboard.html')