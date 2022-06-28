from django.urls import path
from .views import HomeView,PeliculaList

urlpatterns = [
    #pagina principal
    path('Cartelera/',HomeView.as_view()),
    path('peliculas/',PeliculaList.as_view(),name= 'pelicula'),
]
    