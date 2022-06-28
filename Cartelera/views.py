from random import random
from django.http import HttpResponse
from django.shortcuts import render
from  Cartelera.models import Pelicula,Actor,Critica,Director
from django.views.generic import ListView 
from django.views.generic.base import TemplateView
from random import randint


class HomeView(TemplateView):
    template_name = "main.html"
    paginate_by=3
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        """listo las 12 mejores peliculas"""
        context['peliculas']=Pelicula.objects.filter(id=randint(5,18))
        context['top'] = Pelicula.objects.obtenerMejores()
        return context

class PeliculaList(ListView):
    model = Pelicula
    queryset = Pelicula.objects.all()
    paginate_by = 5
    template_name = 'pelicula.html'
