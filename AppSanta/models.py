from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()

    def __str__(self):
       return f"nombre: {self.nombre} - cantdad: {self.cantidad}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
       return f"nombre: {self.nombre} - apellido: {self.apellido} - email {self.email}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
       return f"nombre: {self.nombre} - apellido: {self.apellido} - email: {self.email} - profesion: {self.profesion}"

class Envio(models.Model):
    direccion = models.CharField(max_length=30) 
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField() 

    def __str__(self):
       return f"direccion: {self.direccion} - fecha_de_entrega: {self.fecha_de_entrega} - entregado:{self.entregado}"