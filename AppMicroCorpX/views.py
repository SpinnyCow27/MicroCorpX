from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect, render

from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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
   return render(request, 'Principal/registro.html', {'title':'registro'})

def login(request):
   return render(request, 'Principal/login.html', {'title':'login'})

def tienda(request):
   return render(request, 'Tienda2/tienda.html', {'title':'tienda'})   


# <<<< RANDOM >>>>
#def registerPage(request):
#    if request.user.is_authenticated:
#        return redirect('index2')
#    else:
#        form = CreateUserForm()
#        if request.method == 'POST':
#            form = CreateUserForm(request.POST)
#            if form.is_valid():
#                form.save()
#                user = form.cleaned_data.get('username')
#                messages.success(request, 'Se registró el usuario ' + user)
#                return redirect('login')
#        return render(request, 'registro.html', {'form':form})
#
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