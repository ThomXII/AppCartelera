from cgitb import text
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

    def __str__(self):
        return self.nombre


class Director(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    foto = models.ImageField(blank=True)
    nacimiento = models.DateField()
    bio = models.TextField(max_length=700)
  
    def __str__(self):
        return self.nombre  



class Pelicula(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    genero = models.CharField(max_length=30)
    resumen = models.CharField(max_length=350)
    actores = models.ManyToManyField(Actor,related_name='peliculas')
    lanzamiento = models.PositiveIntegerField()
    director = models.ForeignKey('Director',on_delete=models.RESTRICT,related_name='peliculas')
    puntaje = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])

    def promedio(self):
        promedio = 0
        num = 0
        den = 0
        a=self.criticas_get.all()
        self.save()
        for i in self.a():
            num+=i
            den+=1
        
        promedio=0 if num == 0 else 1(num/(den))
        self.puntaje =round(promedio)
        self.save()
    
    def __str__(self):
        return '{0}''({1})'.format(self.nombre,self.lanzamiento)
    
class Critica(models.Model):
    mail = models.EmailField(max_length=100,unique=True)
    pelicula = models.ForeignKey('Pelicula', on_delete=models.CASCADE,related_name='criticas')
    puntaje = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    resenia = models.TextField(blank=True,max_length=400)
    validacion = models.BooleanField(default=True)
    #falta una clase meta que ordene todo
    #sobrecargar metodo save
    def borrar(self):
        if self.validacion == False:
            self.delete()

    def save(self, *args, **kwargs):
        if self.validacion == False:
            self.delete()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.mail







