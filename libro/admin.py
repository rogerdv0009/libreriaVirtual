from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Libro)
admin.site.register(Carrito)
admin.site.register(Favorito)
admin.site.register(Pedido)
