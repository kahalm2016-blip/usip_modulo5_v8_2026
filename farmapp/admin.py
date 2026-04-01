from django.contrib import admin
from .models import Categoria
from .models import Medicamento
from .models import Paciente
from .models import MedicoEspecialista
from .models import agendarCita

# Register your models here.

class MedicamentoAdmin(admin.ModelAdmin):
    list_display =("nombre_medicamento","categoria","precio","cantidad")
    ordering =["precio"]
    search_fields =["nombre_medicamento"]
    list_filter = ("disponible","precio")

class CitaAdmin(admin.ModelAdmin):
    list_display = ("documento_paciente","fecha_cita","receta_medica")
    search_fields = ["nombre_paciente"]

class MedicoEspecialistaAdmin(admin.ModelAdmin):
    list_display = ("matricula_medico","nombre_medico","contacto")
    search_fields = ["nombre_medico"]

admin.site.register(Categoria)
admin.site.register(Medicamento,MedicamentoAdmin)
admin.site.register(Paciente)
admin.site.register(agendarCita,CitaAdmin)
admin.site.register(MedicoEspecialista,MedicoEspecialistaAdmin)
