#from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from .serializers import *
from .models import *


class ResponsableView(viewsets.ModelViewSet):
    serializer_class = ResponsableSerializer
    queryset = Responsable.objects.all()

class CentroCostoView(viewsets.ModelViewSet):
    serializer_class = CentroCostoSerializer
    queryset = CentroCosto.objects.all()
    
class AreaResponsabilidadView(viewsets.ModelViewSet):
    serializer_class = AreaResponsabilidadSerializer
    queryset = AreaResponsabilidad.objects.all()
    
class SedeView(viewsets.ModelViewSet):
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()
    
class EdificioView(viewsets.ModelViewSet):
    serializer_class = EdificioSerializer
    queryset = Edificio.objects.all()

class LocalView(viewsets.ModelViewSet):
    serializer_class = LocalSerializer
    queryset = Local.objects.all()
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ["nombre", "sede_pertenece", "edificio_pertenece", "funcion", "estado_constructivo"]
    
class ReservacionView(viewsets.ModelViewSet):
    serializer_class = ReservacionSerializer
    queryset = Reservacion.objects.all()

    
             
class Extras(viewsets.ViewSet):

    @action(detail=False)
    def get_all_information(self, request):
        """
            Devuelve de forma organizada todas las informaciones, desde la sede hasta los sublocales
        """
        try:
            sedes = Sede.objects.all()
            sede_data = []

            for sede in sedes:
                edificios = sede.edificios.all()
                edificios_data = []

                for edificio in edificios:
                    locales = edificio.locales.filter(local_pertenece__isnull=True)
                    locales_data = self.get_local_data(locales)
                    edificios_data.append({
                        "id_edificio": edificio.id,
                        "nombre_edificio": edificio.nombre,
                        "locales": locales_data
                    })

                locales_sin_edificio = sede.sede_local.filter(edificio_pertenece__isnull=True, local_pertenece__isnull=True)
                locales_sin_edificio_data = self.get_local_data(locales_sin_edificio)

                sede_data.append({
                    "id_sede": sede.id,
                    "nombre_sede": sede.nombre,
                    "edificios": edificios_data,
                    "locales_sin_edificio": locales_sin_edificio_data
                })
            
            return JsonResponse(sede_data, safe=False)
        except Exception as e:
            return JsonResponse({"error":str(e)}, status=500)


    def get_local_data(self, locales):
        local_data = []

        for local in locales:
            sublocales = local.sublocales.all()
            sublocales_data = self.get_local_data(sublocales)
            local_data.append({
                "id_local": local.id,
                "nombre_local": local.nombre,
                "estado_constructivo": local.estado_constructivo,
                "sublocales": sublocales_data
            })

        return local_data