from django.db import models

# Create your models here.
class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    # imagen_url = models.URLField()
    imagen_url = models.CharField(max_length=200, default="default.png")

    def __str__(self):
        return self.nombre
    