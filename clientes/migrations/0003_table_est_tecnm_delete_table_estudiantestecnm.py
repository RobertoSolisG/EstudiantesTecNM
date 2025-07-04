# Generated by Django 5.2.3 on 2025-06-30 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_table_estudiantestecnm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table_Est_TecNM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NUM', models.IntegerField()),
                ('APELLIDOS', models.CharField(blank=True)),
                ('NOMBRE', models.CharField(blank=True)),
                ('EMAIL', models.CharField(blank=True)),
                ('GENERO', models.CharField(blank=True)),
                ('CONTROL', models.CharField(blank=True)),
                ('TELEFONO', models.CharField(blank=True)),
                ('HORARIO', models.CharField(blank=True)),
                ('INSTITUTO', models.CharField(blank=True)),
                ('CURP', models.CharField(blank=True)),
                ('EDAD', models.CharField(blank=True)),
                ('MODALIDAD', models.CharField(blank=True)),
                ('SEDE', models.CharField(blank=True)),
                ('ACTIVIDAD', models.CharField(blank=True)),
                ('DISCAPACIDAD', models.CharField(blank=True)),
                ('TIPO', models.CharField(blank=True)),
                ('APOYO', models.CharField(blank=True)),
                ('CARRERA', models.CharField(blank=True)),
                ('AVANCE', models.CharField(blank=True)),
                ('PROMEDIO', models.CharField(blank=True)),
                ('EQUIPO', models.CharField(blank=True)),
                ('PROYECTO_INFOTEC', models.CharField(blank=True)),
                ('AREA', models.CharField(blank=True)),
                ('PROYECTO_PROPIO', models.CharField(blank=True)),
                ('OBJETIVO', models.CharField(blank=True)),
                ('DESCRIPCION', models.CharField(blank=True)),
                ('TUTOR', models.CharField(blank=True)),
                ('COTUTOR', models.CharField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Table_EstudiantesTecNM',
        ),
    ]
