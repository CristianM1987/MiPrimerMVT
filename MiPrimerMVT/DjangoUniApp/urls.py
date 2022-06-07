from django.urls import path 
from DjangoUniApp.views import index, agregar,borrar, buscar, form_carga, agregara, agregarv, buscara, borrara

urlpatterns =[
    path('', index, name='index'),
    path('agregar/', agregar, name="agregar"),
    path('agregaranimal/', agregara, name="agregara"),
    path('agregarvegetal/', agregarv, name="agregarv"),
    path('borrar/<identificador>', borrar, name="borrar"),
    path('borrara/<identificador>', borrara, name="borrara"),
    path('buscar/', buscar, name="buscar"),
    path('buscaranimal/', buscara, name="buscara"),
    path('form_carga/', form_carga),
        ]