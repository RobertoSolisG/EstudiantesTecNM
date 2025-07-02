from django.shortcuts import render

from .models import Cliente
from .models import Table_Est_TecNM
from django.db.models import Count
import json

# Create your views here.
def clientes(request):

    clients = Cliente.objects.all()

    return render(request, 'clientes.html', {"clientes":clients})



    # Create your views here.

def estudiantes(request):
    total = Table_Est_TecNM.objects.count()

    por_actividad = Table_Est_TecNM.objects.values('ACTIVIDAD').annotate(y=Count('ACTIVIDAD')).order_by('-y')
    por_institucion = Table_Est_TecNM.objects.values('INSTITUTO').annotate(y=Count('INSTITUTO')).order_by('-y')
    por_sede = Table_Est_TecNM.objects.values('SEDE').annotate(y=Count('SEDE'))
    por_modalidad = Table_Est_TecNM.objects.values('MODALIDAD').annotate(y=Count('MODALIDAD'))
    por_edad = Table_Est_TecNM.objects.values('EDAD').annotate(y=Count('EDAD')).order_by('EDAD')
    genero = Table_Est_TecNM.objects.values('GENERO').annotate(y=Count('GENERO'))
    carrera = Table_Est_TecNM.objects.values('CARRERA').annotate(y=Count('CARRERA'))
    area = Table_Est_TecNM.objects.values('AREA').annotate(y=Count('AREA')).order_by('-y')
    tipos_disca = Table_Est_TecNM.objects.values('TIPO').annotate(y=Count('TIPO')).order_by('-y')

    def formatea(lista, clave):
        return [{"name": e[clave], "y": e["y"]} for e in lista if e[clave]]

    context = {
        "total_estudiantes": total,
        "por_actividad": json.dumps(formatea(por_actividad, 'ACTIVIDAD')),
        "por_institucion": json.dumps(formatea(por_institucion, 'INSTITUTO')),
        "por_sede": json.dumps(formatea(por_sede, 'SEDE')),
        "por_modalidad": json.dumps(formatea(por_modalidad, 'MODALIDAD')),
        "por_edad": json.dumps(formatea(por_edad, 'EDAD')),
        "genero": json.dumps(formatea(genero, 'GENERO')),
        "carrera": json.dumps(formatea(carrera, 'CARRERA')),
        "area": json.dumps(formatea(area, 'AREA')),
        "tipos_disca": json.dumps(formatea(tipos_disca, 'TIPO')),
    }
    return render(request, 'ficha.html', context)