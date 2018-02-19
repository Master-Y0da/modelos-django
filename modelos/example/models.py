from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=40)


class Programador(models.Model):
    nombre = models.CharField(max_length=50)
    compania = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
