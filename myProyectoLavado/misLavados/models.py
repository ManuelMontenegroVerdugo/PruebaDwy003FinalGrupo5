from django.db import models

# Create your models here.


class SliderIndex(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    image = models.ImageField(upload_to='car',null=True)

    def __str__(self):
        return self.ident



class SliderGaleria(models.Model):
    ident1 = models.CharField(max_length=15,primary_key=True)
    image1 = models.ImageField(upload_to='car',null=True)

    def __str__(self):
        return self.ident1



class Insumos(models.Model):
    nombre = models.CharField(max_length=120,primary_key=True)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()


    def __str__(self):
        return self.nombre
    


class MisionyVision(models.Model):
    ident = models.CharField(max_length=120,primary_key=True)
    mision = models.TextField()
    vision = models.TextField()


    def __str__(self):
        return self.ident