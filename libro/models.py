from django.db import models

from user.models import Cliente

# Create your models here.

genero_opt = {
    ("Drama", "Drama"),
    ("Fantasía", "Fantasía"),
    ("Acción", "Acción"),
    ("Comedia", "Comedia"),
}
cantidad_libro = {
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4)
}
class Libro(models.Model):
    foto = models.ImageField('Imagen', upload_to='libro/', max_length=250,null=False, blank=False)
    nombre = models.CharField('Nombre', max_length=50,null=False, blank=False)
    autor = models.CharField('Autor', max_length=50,null=False, blank=False)
    genero = models.CharField("Genero", max_length=50, choices = genero_opt,null=False, blank=False)
    sinopsis = models.TextField('Sinopsis', null=False, blank=False)
    precio = models.PositiveIntegerField("Precio",null=False, blank=False, default=250)
    fecha_publicado = models.DateField("Fecha de Publicación", auto_now=False, auto_now_add=False,null=False, blank=False)
    
    
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["-id"]
        
class Favorito(models.Model):
    user = models.ForeignKey(Cliente, verbose_name='Usuario', on_delete=models.CASCADE,null=False, blank=False)
    libro = models.ForeignKey(Libro, verbose_name="Libro", on_delete=models.CASCADE,null=False, blank=False)
    
    class Meta:
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        ordering = ["-id"]
        
class Carrito(models.Model):
    user = models.ForeignKey(Cliente, verbose_name='Usuario', on_delete=models.CASCADE,null=False, blank=False)
    libro = models.ForeignKey(Libro, verbose_name='Libro', on_delete=models.CASCADE,null=False, blank=False)
    cantidad = models.IntegerField("Cantidad",null=False, blank=False, choices=cantidad_libro)
    revisado = models.BooleanField("Revision", default=False)
    aceptado = models.BooleanField("Aceptacion", default=False)
    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"
        ordering = ["-id"]
        
class Pedido(models.Model):
    carrito = models.ForeignKey(Carrito, verbose_name="Pedido", on_delete=models.CASCADE)
    
