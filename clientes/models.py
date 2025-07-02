from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    edad = models.PositiveSmallIntegerField()


class Table_Est_TecNM(models.Model):
    NUM = models.IntegerField()
    APELLIDOS = models.CharField(null=True,blank=True)
    NOMBRE = models.CharField(null=True,blank=True)
    EMAIL = models.CharField(null=True,blank=True)
    GENERO = models.CharField(null=True,blank=True)
    CONTROL = models.CharField(null=True,blank=True)
    TELEFONO = models.CharField(null=True,blank=True)
    HORARIO = models.CharField(null=True,blank=True)
    INSTITUTO = models.CharField(null=True,blank=True)
    CURP = models.CharField(null=True,blank=True)
    EDAD = models.CharField(null=True,blank=True)
    MODALIDAD = models.CharField(null=True,blank=True)
    SEDE = models.CharField(null=True,blank=True)
    ACTIVIDAD= models.CharField(null=True,blank=True)
    DISCAPACIDAD = models.CharField(null=True,blank=True)
    TIPO = models.CharField(null=True,blank=True)
    APOYO = models.CharField(null=True,blank=True)
    CARRERA = models.CharField(null=True,blank=True)
    AVANCE = models.CharField(null=True,blank=True)
    PROMEDIO = models.CharField(null=True,blank=True)
    EQUIPO= models.CharField(null=True,blank=True)
    PROYECTO_INFOTEC = models.CharField(null=True,blank=True)
    AREA = models.CharField(null=True,blank=True)
    PROYECTO_PROPIO = models.CharField(null=True,blank=True)
    OBJETIVO = models.CharField(null=True,blank=True)
    DESCRIPCION = models.CharField(null=True,blank=True)
    TUTOR = models.CharField(null=True,blank=True)
    COTUTOR = models.CharField(null=True,blank=True)