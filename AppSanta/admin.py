from django.contrib import admin
from AppSanta.models import Producto,Cliente,Envio,Proveedor


# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Envio)
admin.site.register(Proveedor)