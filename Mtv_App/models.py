from django.db import models


"""
Padre(nombre, apellido, nacimiento)
Madre(nombre, apellido, nacimiento)
Hermano(nombre, apellido, nacimiento)
"""




class Padre(models.Model):
    nombre = models.CharField(max_length = 128)
    apellido = models.CharField(max_length= 128)
    nacimiento = models.DateField()


class Madre(models.Model):
    nombre = models.CharField(max_length = 128)
    apellido = models.CharField(max_length= 128)
    nacimiento = models.DateField()


class Hermano(models.Model):
    nombre = models.CharField(max_length = 128)
    apellido = models.CharField(max_length= 128)
    nacimiento = models.DateField()


