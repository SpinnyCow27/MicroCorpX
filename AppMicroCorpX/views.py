from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect, render

from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

# <----- CARPETA PRINCIPAL ----->
def index(request):
   return render(request, 'Principal/index2.html', {'title':'index'})

def index2(request):
   return render(request, 'Principal/index2.html', {'title':'index2'})   

def contacto(request):
   return render(request, 'Principal/contacto.html', {'title':'contacto'})

def registro(request):
   return render(request, 'Principal/registro.html', {'title':'registro'})

def login(request):
   return render(request, 'Principal/login.html', {'title':'login'})

def tienda(request):
   return render(request, 'Tienda2/tienda.html', {'title':'tienda'})   