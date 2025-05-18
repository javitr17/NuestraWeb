from django.urls import path
from .views import *
urlpatterns = [
    
     path('musica', musica.as_view(), name='musica'),
     path('detalles', detalles.as_view(), name='detalles'),
     path('eventos', eventos.as_view(), name='eventos'),
     path('galeria', galeria.as_view(), name='galeria'),



]