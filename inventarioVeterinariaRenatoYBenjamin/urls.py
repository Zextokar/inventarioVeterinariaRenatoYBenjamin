"""
URL configuration for inventarioVeterinariaRenatoYBenjamin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from gestorUser.views import *
from gestorProducts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('dashboard/', Dashboard, name='dashboard'),
    path('productos/', Productos, name='productos'),
    path('insertProducts/', insertProductos, name='insertProducts'),
    path('editProducto/<int:id>', editarProductos, name='editProducto'),
    path('deleteProducto/<int:id>', eliminarProductos, name='deleteProducto'),
    path('categorias/', Categoria, name='categorias'),
    path('insertCategory/', insertCategorias, name='insertCategory'),
    path('editCategory/<int:id>', editarCategoria, name='editCategory'),
    path('deleteCategory/<int:id>', eliminarCategoria, name='deleteCategory'),
    path('usergestion/', Usergestion, name='usergestion'),
    path('insertUser/', InsertUser, name='insertUser'),
    path('editUser/<int:id>', editUser, name='editUser'),
    path('deleteUser/<int:id>', deleteUser, name='deleteUser'),
]
