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

from django.shortcuts import render
from django.db.models import Count
from .models import Table_Est_TecNM
import json
from django.core.serializers.json import DjangoJSONEncoder

def estudiantes(request):
    # Obtener todos los datos
    estudiantes = Table_Est_TecNM.objects.all()

    # Obtener todas las actividades únicas
    actividades = estudiantes.values_list('actividad', flat=True).distinct()

    # Función para contar agrupaciones
    def contar(estudiantes_queryset, campo):
        resultado = (
            estudiantes_queryset
            .values(campo)
            .exclude(**{campo: None})
            .annotate(total=Count(campo))
            .order_by('-total')
        )
        return [[r[campo], r['total']] for r in resultado if r[campo]]

    # Función para construir la estructura por actividad
    datos_por_actividad = {}

    for actividad in actividades:
        filtro = estudiantes.filter(actividad=actividad)
        datos_por_actividad[actividad] = {
            'actividad': contar(filtro, 'actividad'),
            'institucion': contar(filtro, 'instituto'),
            'sede': contar(filtro, 'sede'),
            'modalidad': contar(filtro, 'modalidad'),
            'edad': contar(filtro, 'edad'),
            'genero': contar(filtro, 'genero'),
            'carrera': contar(filtro, 'carrera'),
            'area': contar(filtro, 'area'),
            'tipos_disca': contar(filtro, 'discapacidad'),
        }

    # También agregamos la agrupación "Todas"
    datos_por_actividad["Todas"] = {
        'actividad': contar(estudiantes, 'actividad'),
        'institucion': contar(estudiantes, 'instituto'),
        'sede': contar(estudiantes, 'sede'),
        'modalidad': contar(estudiantes, 'modalidad'),
        'edad': contar(estudiantes, 'edad'),
        'genero': contar(estudiantes, 'genero'),
        'carrera': contar(estudiantes, 'carrera'),
        'area': contar(estudiantes, 'area'),
        'tipos_disca': contar(estudiantes, 'discapacidad'),
    }

    contexto = {
        'datos_por_actividad': json.dumps(datos_por_actividad, cls=DjangoJSONEncoder),
        'actividades_disponibles': [a for a in actividades if a],  # excluye None o vacío
    }

    return render(request, 'ficha.html', contexto)