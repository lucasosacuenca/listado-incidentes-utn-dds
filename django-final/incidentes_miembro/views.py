from django.shortcuts import render
from incidentes_miembro.models import Incidente, Comunidad, Miembro


# Create your views here.

def index(request, id_parameter):
    miembro = Miembro.objects.filter(id=id_parameter).first()
    comunidad = Comunidad.objects.filter(id=miembro.comunidad.id).first()
    incidentes = Incidente.objects.filter(prestacion_servicio=comunidad.pestacion_servicio)
    return render(request, 'lista_incidentes.html', {'incidentes': incidentes, 'miembro':miembro})
