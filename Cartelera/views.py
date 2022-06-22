from django.http import HttpResponse
from django.shortcuts import render
from  .models import Pelicula,Actor,Critica,Director
from django.views.generic import ListView 

def index(request):
    return render(request,'index.html')

def main(request):
    return render(request,'main.html')

def ver_actores(request):
    return render(request,'actores.html')

def home(request):    
    return render(request,'home.html')

class PeliculaList(ListView):
    model = Pelicula
    queryset = Pelicula.objects.all()
    paginate_by = 5
    template_name = 'pelicula.html'
