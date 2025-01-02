from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    

class Telefono(models.Model):
    persona = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE,
        related_name='telefonos',
    )
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.telefono
    