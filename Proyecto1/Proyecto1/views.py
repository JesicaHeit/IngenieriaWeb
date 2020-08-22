from django.http import HttpResponse
from django.template import Template, Context
import datetime

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

