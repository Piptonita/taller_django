from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la persona")
    apellidos = models.CharField(max_length=200, verbose_name="Apellidos", blank=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre 
