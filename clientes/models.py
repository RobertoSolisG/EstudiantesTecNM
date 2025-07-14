from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    edad = models.PositiveSmallIntegerField()


class Table_Est_TecNM(models.Model):
    num = models.IntegerField()
    apellidos = models.CharField(max_length=100,null=True,blank=True)
    nombre = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    genero = models.CharField(max_length=100,null=True,blank=True)
    control = models.CharField(max_length=100,null=True,blank=True)
    telefono = models.CharField(max_length=100,null=True,blank=True)
    horario = models.CharField(max_length=100,null=True,blank=True)
    instituto = models.CharField(max_length=100,null=True,blank=True)
    curp = models.CharField(max_length=100,null=True,blank=True)
    edad = models.CharField(max_length=100,null=True,blank=True)
    modalidad = models.CharField(max_length=100,null=True,blank=True)
    sede = models.CharField(max_length=100,null=True,blank=True)
    actividad = models.CharField(max_length=100,null=True,blank=True)
    discapacidad = models.CharField(max_length=100,null=True,blank=True)
    tipo = models.CharField(max_length=100,null=True,blank=True)
    apoyo = models.CharField(max_length=100,null=True,blank=True)
    carrera = models.CharField(max_length=100,null=True,blank=True)
    avance = models.CharField(max_length=100,null=True,blank=True)
    promedio  = models.CharField(max_length=100,null=True,blank=True)
    equipo = models.CharField(max_length=100,null=True,blank=True)
    proyecto_infotec = models.CharField(max_length=100,null=True,blank=True)
    area = models.CharField(max_length=100,null=True,blank=True)
    proyecto_propio = models.CharField(max_length=100,null=True,blank=True)
    objetivo = models.CharField(max_length=100,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    turor = models.CharField(max_length=100,null=True,blank=True)
    coautor = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        db_table = 'table_est_tecnm'  # <- Aquí le decimos a Django que use la tabla existente