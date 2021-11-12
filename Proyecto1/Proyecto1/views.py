from django.http import HttpResponse
import datetime

def saludo(request):        #Primera vista

    documento= """ <html>
        <body>
            <h1>
                Hola amigos!! Primer pagina en Django
            </h1>
        </body>
    </html>"""
    return HttpResponse(documento)

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
#    edadActual = 18
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
