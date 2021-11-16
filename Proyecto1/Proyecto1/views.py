from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido = apellido

def saludo(request):        #Primera vista

    p1= Persona("Profesor Manuel", "Perez")
    #doc_externo = open("/home/ayzac/Desktop/Django/Proyecto1/Proyecto1/plantillas/index.html")

    #nombre = "Isaac"
    #apellido = "Lopez"

    temasCurso = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

    hoy = datetime.datetime.now()

    #plt= Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo = get_template('index.html')

    #ctx = Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "dia_actual": hoy, "temas":temasCurso})
    #documento =doc_externo.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "dia_actual": hoy, "temas":temasCurso})

    return render(request, "index.html", {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "dia_actual": hoy, "temas":temasCurso})

def cursoc(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "curso.html", {"dameFecha": fecha_actual})

def cursocss (request):
    fecha_actual = datetime.datetime.now()

    return render(request, "cursocss.html", {"dameFecha": fecha_actual})

def despedida(request):
    despedida = """<html>
        <body>
            <h1>
                Adios amigos :3
            </h1>
        </body>
    </html>"""
    return HttpResponse(despedida)

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    date = """ <html>
        <body>
            <h2>
                Fecha y hora actual %s
            </h2>
        </body>
    </html>""" % fecha_actual

    return HttpResponse(date)


def calculaEdad(request, edad, agno):
#    edadActual = 18  comentar
    periodo = agno-2019
    edadFutura = edad + periodo
    documentos = """ <html>
        <body>
            <h2>
                En el año %s tendras %s años
            </h2>
        </body>
    </html>""" % (agno, edadFutura)

    return HttpResponse(documentos)
