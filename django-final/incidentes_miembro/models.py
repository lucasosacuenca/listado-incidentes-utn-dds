# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comunidad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    pestacion_servicio = models.ForeignKey('PrestacionServicio', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunidad'


class Empresa(models.Model):
    id = models.BigIntegerField(primary_key=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    organismo_control = models.ForeignKey('OrganismoControl', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Entidad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    tiempo_cierre_promedio = models.FloatField(blank=True, null=True)
    localizacion = models.ForeignKey('Localizacion', models.DO_NOTHING, blank=True, null=True)
    tipo_entidad = models.ForeignKey('TipoEntidad', models.DO_NOTHING, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidad'


class Establecimiento(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    entidad = models.ForeignKey(Entidad, models.DO_NOTHING, blank=True, null=True)
    localizacion = models.ForeignKey('Localizacion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'establecimiento'


class HibernateSequence(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hibernate_sequence'


class HorariosDisponiblesNotificacion(models.Model):
    notificacion = models.ForeignKey('Notificacion', models.DO_NOTHING)
    horarios_disponibles = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horarios_disponibles_notificacion'


class HorariosDisponiblesPersona(models.Model):
    persona = models.ForeignKey('Persona', models.DO_NOTHING)
    horarios_disponibles = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horarios_disponibles_persona'


class Incidente(models.Model):
    id = models.BigIntegerField(primary_key=True)
    detalle = models.CharField(max_length=255, blank=True, null=True)
    esta_resuelto = models.BooleanField(blank=True, null=True)  # This field type is a guess.
    fecha_apertura = models.DateTimeField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    cerrador = models.ForeignKey('Miembro', models.DO_NOTHING, blank=True, null=True)
    iniciador = models.ForeignKey('Miembro', models.DO_NOTHING, related_name='incidente_iniciador_set', blank=True, null=True)
    prestacion_servicio = models.ForeignKey('PrestacionServicio', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidente'


class Localizacion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)
    municipio = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localizacion'


class Miembro(models.Model):
    id = models.BigIntegerField(primary_key=True)
    rol = models.CharField(max_length=255, blank=True, null=True)
    comunidad = models.ForeignKey(Comunidad, models.DO_NOTHING, blank=True, null=True)
    persona = models.ForeignKey('Persona', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'miembro'


class Notificacion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    datos = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    medio = models.CharField(max_length=255, blank=True, null=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'


class OrganismoControl(models.Model):
    id = models.BigIntegerField(primary_key=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organismo_control'


class Persona(models.Model):
    id = models.BigIntegerField(primary_key=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    fechadenacimiento = models.DateTimeField(db_column='fechaDeNacimiento', blank=True, null=True)  # Field name made lowercase.
    formanotificacion = models.CharField(db_column='formaNotificacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    medionotificacion = models.CharField(db_column='medioNotificacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=255, blank=True, null=True)
    numerodedocumento = models.IntegerField(db_column='numeroDeDocumento', blank=True, null=True)  # Field name made lowercase.
    localizacion = models.ForeignKey(Localizacion, models.DO_NOTHING, blank=True, null=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    servicio = models.ForeignKey('Servicio', models.DO_NOTHING, blank=True, null=True)
    entidad = models.ForeignKey(Entidad, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'


class PrestacionServicio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    establecimiento = models.ForeignKey(Establecimiento, models.DO_NOTHING, blank=True, null=True)
    servicio = models.ForeignKey('Servicio', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestacion_servicio'


class Reporte(models.Model):
    id = models.BigIntegerField(primary_key=True)
    detalle = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    miembro = models.ForeignKey(Miembro, models.DO_NOTHING, blank=True, null=True)
    incidente = models.ForeignKey(Incidente, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporte'


class Servicio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio'


class TipoEntidad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    tipo_entidad = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_entidad'


class Usuario(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contrasenia = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    rol = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
