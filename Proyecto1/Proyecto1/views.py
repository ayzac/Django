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


def calculaEdad(request, agno):
    edadActual = 18
    periodo = agno-2019
    edadFutura = edadActual + periodo
