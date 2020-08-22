from django.http import HttpResponse
from django.template import Template, Context
import datetime
def saludo(request): #Vista
    nombre="Juancito Perez"
    ahora=datetime.datetime.now()
    doc_externo= open("C:/IngenieriaWeb/Proyecto1/Proyecto1/plantillas/plantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx= Context({"nombre_persona": nombre, "hora_actual":ahora})
    documento=plt.render(ctx)

    return HttpResponse(documento)