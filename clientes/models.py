from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    edad = models.PositiveSmallIntegerField()


class Table_Est_TecNM(models.Model):
    NUM = models.IntegerField()
    APELLIDOS = models.CharField(max_length=100,null=True,blank=True)
    NOMBRE = models.CharField(max_length=100,null=True,blank=True)
    EMAIL = models.CharField(max_length=100,null=True,blank=True)
    GENERO = models.CharField(max_length=100,null=True,blank=True)
    CONTROL = models.CharField(max_length=100,null=True,blank=True)
    TELEFONO = models.CharField(max_length=100,null=True,blank=True)
    HORARIO = models.CharField(max_length=100,null=True,blank=True)
    INSTITUTO = models.CharField(max_length=100,null=True,blank=True)
    CURP = models.CharField(max_length=100,null=True,blank=True)
    EDAD = models.CharField(max_length=100,null=True,blank=True)
    MODALIDAD = models.CharField(max_length=100,null=True,blank=True)
    SEDE = models.CharField(max_length=100,null=True,blank=True)
    ACTIVIDAD= models.CharField(max_length=100,null=True,blank=True)
    DISCAPACIDAD = models.CharField(max_length=100,null=True,blank=True)
    TIPO = models.CharField(max_length=100,null=True,blank=True)
    APOYO = models.CharField(max_length=100,null=True,blank=True)
    CARRERA = models.CharField(max_length=100,null=True,blank=True)
    AVANCE = models.CharField(max_length=100,null=True,blank=True)
    PROMEDIO = models.CharField(max_length=100,null=True,blank=True)
    EQUIPO= models.CharField(max_length=100,null=True,blank=True)
    PROYECTO_INFOTEC = models.CharField(max_length=100,null=True,blank=True)
    AREA = models.CharField(max_length=100,null=True,blank=True)
    PROYECTO_PROPIO = models.CharField(max_length=100,null=True,blank=True)
    OBJETIVO = models.CharField(max_length=100,null=True,blank=True)
    DESCRIPCION = models.CharField(max_length=100,null=True,blank=True)
    TUTOR = models.CharField(max_length=100,null=True,blank=True)
    COTUTOR = models.CharField(max_length=100,null=True,blank=True)