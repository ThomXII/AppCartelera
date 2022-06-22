from django.urls import path
from .views import home,ver_actores,index,PeliculaList,main

urlpatterns = [
    #pagina principal
    path('main/',main,name='main'),
    path('index/',index,name='index'),
    path('peliculas/',PeliculaList.as_view(),name= 'pelicula'),
    path('home/',home,name='home'),
    path('actores/',ver_actores,name='actores'),
]