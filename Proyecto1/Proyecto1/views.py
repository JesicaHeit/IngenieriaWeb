from django.http import HttpResponse
from django.template import Template, Context
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
import datetime
from django.shortcuts import render
from Proyecto1.forms import CustomUserForm

def inicio_sesion(request):
    data = {
        'form': CustomUserForm()
    }
    doc_externo = open("C:/IngenieriaWeb/Proyecto1/Proyecto1/templates/registration/login.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def registro_usuario(request):
    data = {
        'form': CustomUserForm()
    }
    doc_externo = open("C:/IngenieriaWeb/Proyecto1/Proyecto1/plantillas/plantilla_registro.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)
    #return render(request, aca va template, data)


def home(request): #Inicio
    nombre = "Juancito Perez"
    ahora = datetime.datetime.now()
    doc_externo = open("C:/IngenieriaWeb/Proyecto1/Proyecto1/plantillas/plantilla_home.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona": nombre, "hora_actual": ahora})
    documento = plt.render(ctx)
    return HttpResponse(documento)


def recipes(request): #Página recetas - Necesita login
    nombre = "Ana"
    ahora = datetime.datetime.now()
    doc_externo = open("C:/IngenieriaWeb/Proyecto1/Proyecto1/plantillas/plantilla_recipes.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona": nombre, "hora_actual": ahora})
    documento = plt.render(ctx)

    return HttpResponse(documento)



"""
def saludo(request): #Vista
    nombre="Juancito Perez"
    ahora=datetime.datetime.now()
    doc_externo= open("C:/IngenieriaWeb/Proyecto1/Proyecto1/plantillas/plantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx= Context({"nombre_persona": nombre, "hora_actual":ahora})
    documento=plt.render(ctx)

    return HttpResponse(documento)
"""

