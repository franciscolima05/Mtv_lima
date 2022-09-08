from django.http import HttpResponse
from django.template import Template, Context
from Mtv_App.models import Padre, Madre, Hermano



def probar_template(request):
    with open (r'C:\Users\Francisco\Desktop\Python\Trabajos\Django\Mtv-Lima\MTV\MTV\templates\template.html') as archivo:
        
        plantilla = Template(archivo.read())
    
    papa = Padre.objects.all()

    mama = Madre.objects.all()

    hermanito = Hermano.objects.all()

    diccionario =[papa, mama, hermanito]

    documento_html  = plantilla.render(diccionario)

    return HttpResponse(documento_html)