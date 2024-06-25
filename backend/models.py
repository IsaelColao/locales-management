from django.db import models

# Create your models here.

class Responsable (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, null=True, blank=True)
    carnet = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nombre

class CentroCosto (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    responsable = models.ForeignKey(Responsable, on_delete = models.PROTECT, max_length=100)
    
    def __str__(self):
        return self.nombre

class AreaResponsabilidad (models.Model):
    id = models.AutoField(primary_key=True)
    centro_pertenece = models.ForeignKey(CentroCosto, on_delete = models.PROTECT)
    nombre = models.CharField(max_length=100)
    responsable = models.ForeignKey(Responsable, on_delete = models.PROTECT, max_length=100)
    
    def __str__(self):
        return self.nombre

class Sede (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
class Edificio (models.Model):
    id = models.AutoField(primary_key=True)
    sede_pertenece = models.ForeignKey(Sede, on_delete = models.PROTECT, related_name="edificios")
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    niveles = models.IntegerField()
    subnivel = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre

class Local (models.Model):
    id = models.AutoField(primary_key=True)
    sede_pertenece = models.ForeignKey(Sede, on_delete = models.PROTECT, related_name="sede_local")
    edificio_pertenece = models.ForeignKey(Edificio, on_delete = models.PROTECT,blank=True, null=True,related_name="locales")
    nivel_pertenece = models.IntegerField()
    local_pertenece = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="sublocales")
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    funcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    area_responsab = models.ForeignKey(AreaResponsabilidad, on_delete = models.PROTECT)
    estado_constructivo = models.CharField(max_length=100)
    observaciones = models.TextField(null=True, blank=True)
    reservable = models.BooleanField()
    largo = models.FloatField(null=True)
    ancho = models.FloatField(null=True)
    alto = models.FloatField(null=True)
    
    def __str__(self):
        return self.nombre
    
    
class Reservacion (models.Model):
    id = models.AutoField(primary_key=True)
    local = models.ForeignKey(Local, on_delete = models.PROTECT)
    nombre = models.CharField(max_length=100)
    cargo_reserv = models.CharField(max_length=100)
    inicio_reserva = models.DateField()
    final_reserva = models.DateField(null=False)
    uso_reserv = models.CharField(max_length=100)
    
    def __str__(self):
        return self.id
    
#No creo q sea así esto
class Usuario (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    nivel = models.IntegerField()

    
"""  
Aclaraciones:

- Edificio solamente tiene a Sede como llave foranea
- Nivel solamente tiene a Edificio como llave foranea
- Local tiene a Sede y a Nivel porque si pertenece a la sede no necesariamente tiene que pertenecer a un nivel de un edificio.
- Se entiende como el nivel principal de los edificios y la sede como 1. Para los casos en los que los edificios estan 
  levantados del piso el nivel será 0(ese sera como un subnivel).
- Los datos de la persona que reserva están incluidos en la clase Reservacion, no hay necesidad de hacen una nueva clase para eso.
- Los atributos 'on_delete' serán PROTECT hasta que se demuestre lo contrario.
- Debido a la implementación en Django, si los atributos largo y ancho de local no se introducen, automáticamente se les asignarán 
  los valores de 1.0 respectivamente.

-* Hace falta aclarar si los locales podrán tener locales dentro.

-* Si el atributo subnivel de edificio esta en True los niveles empezaran en 0, si esta en False empezaran en 1.

"""