from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
rol_user ={
    ("trabajador", "trabajador"),
    ("cliente", "cliente"),
    ("jefe", "jefe")
}
class Cliente(AbstractUser):
    rol=models.CharField("Rol", max_length=50, choices=rol_user)
    billetera = models.PositiveIntegerField("Billetera",null=False, blank=False, default=1000)