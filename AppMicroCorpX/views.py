from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect, render
from django.views.generic.edit import FormView

from django import forms
from AppMicroCorpX.forms import CreateUserForm, ClienteForm
#from AppMicroCorpX.models import Cliente, Venta, Venta_producto, Producto, Genero_producto, Comprobante_pago, Tipo_pago

#Imports para el manejo de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required








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

def login(request):
    if request.user.is_authenticated:
        return redirect('index2')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('index2')
            else:
                messages.info(request,'Usuario o contraseña incorrectas')
        return render(request,'Principal/login.html')

def tienda(request):
   return render(request, 'Tienda2/tienda.html', {'title':'tienda'})   


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


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Usuario o contraseña incorrectas')
        return render(request,'login.html')