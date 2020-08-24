from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
import datetime
from django.shortcuts import render
from Proyecto1.forms import CustomUserForm


def home(request): #Inicio
    nombre = "Juancito Perez"
    ahora = datetime.datetime.now()
    doc_externo = open("C:/IngenieriaWeb/Proyecto1/Proyecto1/plantillas/plantilla_home.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona": nombre, "hora_actual": ahora})
    documento = plt.render(ctx)
    return HttpResponse(documento)

#@login_required(login_url='/accounts/login/')
#@login_required(redirect_field_name='/recipes')
@login_required()
def recipes(request): #Página recetas - Necesita login
    nombre = "Ana"

    ahora = datetime.datetime.now()
    doc_externo = open("C:/IngenieriaWeb/Proyecto1/Proyecto1/plantillas/plantilla_recipes.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona": nombre, "hora_actual": ahora})
    documento = plt.render(ctx)

    return HttpResponse(documento)


def pantalla_intermedia(request): #Vista
    nombre="Tu registro fue exitoso"
    #ahora=datetime.datetime.now()
    doc_externo= open("C:/IngenieriaWeb/Proyecto1/users/templates/users/pantalla_intermedia.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx= Context({"nombre_persona": nombre})
    documento=plt.render(ctx)

    return HttpResponse(documento)



