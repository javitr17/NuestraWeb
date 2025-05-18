
from django.shortcuts import render
from django.views.generic import TemplateView



class musica(TemplateView):
     template_name = 'weblu/musica.html'

class detalles(TemplateView):
     template_name = 'weblu/detalles.html'

class eventos(TemplateView):
     template_name = 'weblu/eventos.html'

class galeria(TemplateView):
     template_name = 'weblu/galeria.html'
