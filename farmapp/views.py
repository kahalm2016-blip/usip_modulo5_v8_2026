from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Categoria
from .models import Medicamento
from .models import Paciente
from .models import MedicoEspecialista
from .models import agendarCita
from .serializers import CategoriaSerializer
from .serializers import MedicamentosSerializer
from .serializers import PacienteSerializer
from .serializers import MedicoEspecialistaSerializer
from .serializers import agendarCitaSerializer
# Create your views here.

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicamentosViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentosSerializer

class MedicoEspecialistaViewSet(viewsets.ModelViewSet):
    queryset = MedicoEspecialista.objects.all()
    serializer_class = MedicoEspecialistaSerializer

class AgendarCitaViewSet(viewsets.ModelViewSet):
    queryset = agendarCita.objects.all()
    serializer_class = agendarCitaSerializer

class MedicamentosCreateAndList(generics.CreateAPIView,generics.ListAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentosSerializer

class PacienteCreateAndList(generics.CreateAPIView,generics.ListAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

@api_view(["GET"])
def paciente_contador(request):
    """
    Cantidad de pacientes registrados
    """
    try:
        cantidad = Pacientes.objects.count()
        return JsonResponse(
            {
                "Total de Pacientes Registrados": cantidad,
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje: ": str(e)},status=400)


@api_view(["GET"])
def medicamentos_tipo(request):
    """
    Cantidad de items en el modelo Producto
    """
    try:
        medicamentos = Medicamentos.objects.filter(categoria='antigripales')
        return JsonResponse(
            ProductoSerializer(medicamentos, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)
