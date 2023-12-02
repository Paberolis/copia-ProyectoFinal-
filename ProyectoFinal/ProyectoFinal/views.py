from django.http import HttpResponse
import datetime
from django.template import  Template, Context
from django.template import loader


#Esta es una vista.
def saludo(request):

    return HttpResponse("Hola  a todos los que me leen")


def despedida(request):
    
    nombre="Juan"
    apellido="Diaz"
    ahora=datetime.datetime.now()
    
    Template_1= loader.get_template("mi_pagina.html")
    
    #ctx=Context({"nombre_persona":nombre, "apellido_persona": apellido, "Fecha_Actual":ahora})

    Style=Template_1.render({"nombre_persona":nombre, "apellido_persona": apellido, "Fecha_Actual":ahora})

    return HttpResponse(Style)


def datenow(request):
    
    now=datetime.datetime.now()

    Style = "<html><body><h2>Fecha y Hora Actuales %s</h2></body></html>" % now.date

    return HttpResponse(Style)


def age(request, edad, anio):
    
    #EdadActual=18
    Periodo=anio-2023
    edadFutura=edad+Periodo
    Style = "<html><body><h2>En el año %s Tendras %s años</h2></body></html>" %(anio, edadFutura)

    return HttpResponse(Style)