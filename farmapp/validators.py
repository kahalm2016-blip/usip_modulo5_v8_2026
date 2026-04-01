from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
def validar_DocumentoPaciente(value):
    if len(value) != 11:
        raise ValidationError('Debe Ingresar la Extension del CI ')

def validar_Cantidad(value):
    if value <= 0:
        raise ValidationError("La Cantidad no puede ser menor o igual a Cero")

def validar_nombre_medicamento(value):
    if len(value)<10:
        raise ValidationError("Debe ingresar Un nombre valido para el medicamento.")

def validar_Contacto(value):
    if value.isdigit()==False:
        raise ValidationError("Debe Ingresar Solamente Numeros.")
