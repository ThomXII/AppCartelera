from cgitb import text
from distutils.command.upload import upload
from tabnanny import verbose
from wsgiref import validate
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models 

# Create your models here.

class Actor(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    foto = models.ImageField(blank=True)
    nacimiento = models.DateField()
    bio = models.TextField(max_length=700)

    class Meta:
        verbose_name=('Actor')
        verbose_name_plural=('Actores')
    def __str__(self):
        return self.nombre


class Director(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    foto = models.ImageField(blank=True)
    nacimiento = models.DateField()
    bio = models.TextField(max_length=700)
    class Meta:
        verbose_name=('Director')
        verbose_name_plural=('Directores')
    def __str__(self):
        return self.nombre  

#funcion para que me devuelva las 12 mejores peliculas
class PeliculaManager(models.Manager):
    def obtenerMejores(self):
        return self.all().order_by('-puntaje')[:12]

class Pelicula(models.Model):
    objects = PeliculaManager()
    nombre = models.CharField(max_length=100,unique=True)
    genero = models.CharField(max_length=30)
    resumen = models.CharField(max_length=350)
    foto= models.ImageField(null=True,blank=True,upload_to="Pelis")
    actores = models.ManyToManyField(Actor,related_name='peliculas')
    lanzamiento = models.PositiveIntegerField()
    director = models.ForeignKey('Director',on_delete=models.RESTRICT,related_name='peliculas')
    puntaje = models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    """def para tener el promedio"""
    def get_promedio(self):
        juntarcriticas=self.critica_set.all()
        cantidad_Criticas=0
        sum=0
        for c in juntarcriticas:
            cantidad_Criticas+=1
            sum+=c.puntaje
        promedio=0 if (sum == 0) else (sum/cantidad_Criticas)
        self.puntaje=promedio
        self.save()
    
    def __str__(self):
        return '{0}''({1})'.format(self.nombre,self.lanzamiento)
    
class Critica(models.Model):
    mail = models.EmailField(max_length=100,unique=True)
    pelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE)
    puntaje = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    resenia = models.TextField(blank=True,max_length=400)
    validacion = models.BooleanField(default=True)
    #sobrecargar metodo save
    """def save(self):
        critica=super().save()
        self.pelicula.promedio()
        return critica"""
    def save(self, *args, **kwargs):
        guarda=super().save()
        self.pelicula.get_promedio()
        return guarda


    def __str__(self):
        return self.mail







