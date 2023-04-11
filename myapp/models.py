from django.db import models
from . import views
# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=255)
    correo = models.EmailField()
    tipoUsuario = models.CharField(max_length=1)
    
    def __str__(self):
        return self.nombre
