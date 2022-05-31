from pyexpat import model
from django.core.validators import MaxValueValidator, MinValueValidator
from re import M
from django.db import models 
from django.forms import CharField

# Create your models here.

class Actor(models.Model):
    nombre_Actor = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    foto_Actor = models.ImageField(blank=True)
    anio_nacimiento = models.DateField()
    resumen_Bibliografico = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.nombre_Actor + " ;"+self.nacionalidad+ " ;"+self.anio_nacimiento+" ;"+self.resumen_Bibliografico


class Director(models.Model):
    nombre_Director = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    foto_Director = models.ImageField(blank=True)
    anio_nacimiento = models.DateField()
    resumen_Bibliografico = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.nombre_Director+" ;"+self.nacionalidad+" ;"+self.anio_nacimiento+" ;"+self.resumen_Bibliografico

    



class Pelicula(models.Model):
    genero = models.CharField(max_length=30)
    nombre = models.Field.primary_key=True
    resumen = models.CharField(max_length=350)
    actores = models.ManyToManyField(Actor)
    anio_de_Lanzamiento = models.DateField()
    director = models.ForeignKey(Director,on_delete=models.RESTRICT)
    puntaje = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])

    def calcular_Puntaje(self):
        todos = 0
        puntajes = 0
        lista_Puntajes = self.critica.all()

        for i in lista_Puntajes:
            puntajes = puntajes +1
            todos = todos + i.puntaje
        promedio = todos // puntajes
    def __listar_Actores(self):
        lista_Actores = ""
        for i in lista_Actores:
            lista_Actores+= Actor.nombre_Actor+" ;"
        return lista_Actores
    
    def __str__(self) -> str:
        return self.genero+" ;"+self.nombre+" ;"+self.resumen+" ;"+self.actores+" ;"+self.director+" ;"+self.anio_de_Lanzamiento+" ;"+self.puntaje


class Critica(models.Model):
    mail = models.EmailField(max_length=100)
    nombre_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    resenia = models.CharField(max_length=400)
    
    def save(self, *args, **kwargs):
        super(Critica, self).save(*args, **kwargs)
    def __tenerpeli(self):
        return self.nombre_pelicula.nombre

    def __str__(self) -> str:
        return self.mail+" ;"+self.__tenerpeli()+" ;"+str(self.puntaje)+" ;"+self.resenia


class Administrador(models.Model):
    usuario_Admin = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.usuario_Admin+" ;"+self.contrasenia
        




