from rest_framework import serializers
from .models import Categoria
from .models import Medicamento
from .models import Paciente
from .models import MedicoEspecialista
from .models import agendarCita


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class MedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = "__all__"
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"
class MedicoEspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicoEspecialista
        fields = "__all__"
class agendarCitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendarCita
        fields = "__all__"
