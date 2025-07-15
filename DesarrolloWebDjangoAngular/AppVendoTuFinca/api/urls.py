from django.urls import path,include
from AppVendoTuFinca.api.views import finca_list,finca_detalle

urlpatterns = [
    path('list/', finca_list, name='fincas-list'),
    path('<int:id>', finca_detalle, name='finca-detalle' ),
]
