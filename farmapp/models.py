from django.db import models
from django.conf import settings
from .validators import validar_DocumentoPaciente
from .validators import validar_Cantidad
from .validators import validar_Contacto
from .validators import validar_Cantidad
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "Categoria - %s" % self.nombre

class Medicamento(models.Model):
    nombre_medicamento = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    cantidad = models.IntegerField(default=0, validators = [validar_Cantidad,])
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Medicamento - %s" % self.nombre_medicamento

class GeneroClas(models.TextChoices):
    M = 'M', 'Masculino'
    F = 'F', 'Femenino'
    O = 'O', 'Otro'

class Paciente(models.Model):
    documento_paciente = models.CharField(max_length = 35,unique=True, validators =[validar_DocumentoPaciente,])
    nombre_paciente = models.CharField(max_length= 75)
    paterno_paciente = models.CharField(max_length= 75)
    materno_paciente = models.CharField(max_length= 75)
    genero = models.CharField(
        max_length=5,
        choices= GeneroClas.choices,
        default=GeneroClas.M
    )
    contacto = models.CharField(max_length=25, validators =[validar_Contacto,])
    email = models.CharField(max_length = 50)
    def __str__(self):
        return "Paciente:" + '-' + self.documento_paciente


class MedicoEspecialista(models.Model):
    matricula_medico = models.CharField(max_length=35)
    nombre_medico = models.CharField(max_length=75)
    paterno_medico = models.CharField(max_length=75)
    materno_medico = models.CharField(max_length=75)
    genero = models.CharField(
        max_length=5,
        choices= GeneroClas.choices,
        default=GeneroClas.M
    )
    contacto = models.CharField(max_length=25, validators =[validar_Contacto,])
    email = models.CharField(max_length = 50)
    def __str__(self):
        return "Especialista:" + '-' + self.nombre_medico

class agendarCita(models.Model):
    documento_paciente = models.ForeignKey(Paciente, null = False, blank = False, on_delete = models.CASCADE)
    costo_cita = models.DecimalField(decimal_places=2, max_digits=10)
    fecha_cita = models.DateField(auto_now_add=True)
    receta_medica = models.CharField(max_length = 50)
    def __str__(self):
        return "Paciente:" + str(self.documento_paciente) + self.receta_medica
