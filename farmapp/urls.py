from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r"categorias",views.CategoriaViewSet)
router.register(r"medicamentos",views.MedicamentosViewSet)
router.register(r"medicoespecialista",views.MedicoEspecialistaViewSet)
router.register(r"agendarcita",views.AgendarCitaViewSet)
router.register(r"paciente",views.PacienteViewSet)

urlpatterns = [

    path('medicamentos/create_list',views.MedicamentosCreateAndList.as_view(),name='medicamentos'),
    path('paciente/create_list',views.PacienteCreateAndList.as_view(),name='pacientes'),
    path('paciente/cantidad',views.paciente_contador),
    path('medicamentos/tipo/categoria',views.medicamentos_tipo),
    path('',include(router.urls))
]
