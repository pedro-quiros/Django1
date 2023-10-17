from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es: {nombre}"
    return HttpResponse(documentoDeTexto)
    

