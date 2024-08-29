from django.http import HttpResponse
from datetime import date
from django.template import Template, Context
from django.template import loader
from AppSanta.models import Producto


def saludo(request):
    return HttpResponse("Hola Santa Ines")

def otra_vista(request):
    return HttpResponse("<h1>SANTA INES SALAZONES</h1><p>Come sano,come bien.</p>")

def dia_de_hoy(request):
    hoy= date.today()
    return HttpResponse(F"Hoy es {hoy}")

def muestra_nombre(self, nombre):
    return HttpResponse(f"Bienvenido {nombre} a Santa Ines.")

def probando_template(request):
    nom= "Ivana"
    ap= "Cussatti"

    diccionario= {"nombre":nom, "apellido": ap}

    #mi_html= open('C:/Users/usuario/OneDrive/Escritorio/ProyectoSantai/Proyecto1/plantillas/template1.html')
    #plantilla = Template(mi_html.read())
    #mi_html.close()
    #mi_contexto= Context()
    plantilla= loader.get_template('template1.html')
    documento= plantilla.render(diccionario)

    return HttpResponse(documento)


def agregar_producto(request,nom,can):
    producto = Producto (nombre=nom, cantidad=can)
    producto.save()

    return HttpResponse ("Producto seleccionado")