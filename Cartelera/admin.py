"""User admin classes"""
from django.contrib import admin
from .models import Pelicula,Actor,Director,Critica
# Register your models here.
"""Admin para Pelicula"""
@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    #orden de como van las cosas
    fields = ["nombre","genero","resumen","lanzamiento","director","actores"]
    #muestra en pantalla listado por id nombre genero y lanzamiento
    list_display = ("id","nombre","genero","lanzamiento")
    #ordena segun el nombre
    ordering = ('nombre',)
    #permite la busqueda o por id o por nombre
    search_fields = ('nombre','id')
    #solo permite acceder si clickeas el nombre
    list_display_links = ("nombre",)
    #aparece un listado al lado para filtrar por genero y por el anio de lanzamiento
    list_filter=("genero","lanzamiento",)
    #paginacion
    list_per_page = 10
    #saco de la parte de add puntaje para q no puegan agregar el puntaje q quieran
    exclude = ("puntaje",)
#admin.site.register(Pelicula),otra forma de registrar
#las funciones de las clases de abajo son las mismas.




"""Admin para Critica"""
@admin.register(Critica)
class CriticaAdmin(admin.ModelAdmin):
    list_display = ("mail","pelicula","puntaje")
    ordering = ('mail',)
    search_fields = ("pelicula","mail",)
    list_display_links = ("mail",)
    list_filter = ("pelicula","puntaje",)
    list_per_page = 10



"""Admin para Actor"""
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    #el [] es otra forma de meter los datos, como una lista
    list_display = ["id","nombre","nacionalidad"]
    ordering = ['id','nombre']
    search_fields = ['id','nombre']
    list_display_links = ['nombre']
    list_filter = ['nacionalidad','peliculas']
    list_per_page = 10

"""Admin para Director"""
@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','nacionalidad']
    ordering = ['id','nombre']
    search_fields = ['id','nombre']
    list_display_links = ['nombre']
    #filtro por las peliculas que tiene
    list_filter = ['peliculas']
    list_per_page = 10

