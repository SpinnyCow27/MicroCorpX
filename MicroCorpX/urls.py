"""MicroCorpX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from AppMicroCorpX import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('registro/', views.registro, name="registro"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('perfil/', views.perfil, name="perfil"),
    path('index2/', views.index2, name="index2"),
    path('tienda', views.tienda, name='tienda'),

    #Producto
    path('crea_producto/', views.crea_producto, name="crea_producto"),
    path('edita_producto/', views.edita_producto, name="edita_producto"),

    #Password Reset
    #urls actualizar password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='Reset_password/password_reset.html'), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='Reset_password/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='Reset_password/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Reset_password/password_reset_complete.html'), name="password_reset_complete"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
