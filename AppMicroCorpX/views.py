from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect, render
from django.views.generic.edit import FormView

from AppMicroCorpX.models import *
from django import forms
from AppMicroCorpX.forms import CreateUserForm, ClienteForm, ProductoForm
#from AppMicroCorpX.models import Cliente, Venta, Venta_producto, Producto, Genero_producto, Comprobante_pago, Tipo_pago

#Imports para el manejo de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test








# Create your views here.
# <-----   REDIRECCIONES   ----->
# <----- CARPETA PRINCIPAL ----->
def index(request):
   return render(request, 'Principal/index2.html', {'title':'index'})

def index2(request):
   return render(request, 'Principal/index2.html', {'title':'index2'})   

def contacto(request):
   return render(request, 'Principal/contacto.html', {'title':'contacto'})

def registro(request):
    if request.user.is_authenticated:
        return redirect('index2')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Se registró el usuario ' + user)
                return redirect('login')
        return render(request, 'Principal/registro.html', {'form':form})

def logoutUser(request):
    logout(request)
    return redirect('login')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/index2')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password=password)

            if user is not None:
                login(request,user)
                return redirect('/index2')
            else:
                messages.info(request,'Usuario o password incorrecto')
        return render(request,'Principal/loginPage.html')


def tienda(request):
    return render(request, 'Tienda2/tienda.html', {'title':'tienda'})   

def tienda6(request):
    form = ProductoForm()
    producto = Producto.objects.all()

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/productos')
            except:
                pass
    else:
        form = ProductoForm()

    context = {'form':form, 'producto': producto}
    return render(request, 'Tienda2/tienda6.html',context)

    
@login_required(login_url='login')
def perfil(request):
    #user = request.GET['username']
    return render(request, 'Principal/perfil.html')
    #Este me trae individualmente al usuario que estoy ocupando x ID
    #user = request.GET['username', 'first_name', 'last_name', 'email']
    #Este me trae los datos del usuario
    #context = {'user':user}

@login_required(login_url='login')
@user_passes_test((lambda u: u.is_superuser),login_url='login')
def crea_producto(request):
    form = ProductoForm()
    productos = Producto.objects.all()

    if request.method == 'POST':
        print(request.POST)
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('index2')
            except:
                pass
        else:
            form = ProductoForm
    context = {'form':form, 'productos':productos}
    return render(request, 'Producto/crea_producto.html', context)

@login_required(login_url='login')
@user_passes_test((lambda u: u.is_superuser),login_url='login')
def edita_producto(request):
    return render(request, 'Producto/edita_producto.html')

@login_required(login_url='login')
def productos(request):
    form = ProductoForm()
    producto = Producto.objects.all()

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/productos')
            except:
                pass
    else:
        form = ProductoForm()

    context = {'form':form, 'producto': producto}
    return render(request, 'productos.html',context)


    


#@login_required(login_url='login')
#def editar(request,id):
#    cli = Cliente.objects.get(id_cliente=id)
#    form = ClienteForm(instance=cli)
#    return render(request,'edit.html', {'form':form, 'id_cliente':cli.id_cliente})


# <<<< RANDOM >>>>
#def index10(request):
#
#    form = ClienteForm()
#    clientes = Cliente.objects.all()
#
#    if request.method == 'POST':
#        print(request.POST)
#        form = ClienteForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('index')
#
#    context = {'form':form, 'clientes':clientes}
#    return render(request, 'AppEjCrud/index.html', context)


#def loginPage(request):
#    if request.user.is_authenticated:
#        return redirect('index')
#    else:
#        if request.method == 'POST':
#            username = request.POST.get('username')
#            password = request.POST.get('password')
#
#            user = authenticate(request, username=username, password=password)
#
#            if user is not None:
#                login(request,user)
#                return redirect('index')
#            else:
#                messages.info(request,'Usuario o contraseña incorrectas')
#        return render(request,'loginPage.html')


#def login(request):
#    if request.user.is_authenticated:
#        return redirect('index2')
#    else:
#        if request.method == 'POST':
#            username = request.POST.get('username')
#            password = request.POST.get('password')
#
#            user = authenticate(request, username=username, password=password)
#
#            if user is not None:
#                login(request,user)
#                return redirect('index2')
#            else:
#                messages.info(request,'Usuario o contraseña incorrectas')
#        return render(request,'Principal/login.html')