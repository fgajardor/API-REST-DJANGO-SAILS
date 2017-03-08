from django.db import models

class Mesa(models.Model):
	nombre = models.CharField(max_length=10)
	tipoPedido = models.CharField(max_length=20)
	valor = models.IntegerField()

	def __str__(self):
		return self.nombre
