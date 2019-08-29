from django.db import models

# Create your models here.
class Microrna(models.Model):
	name = models.CharField(max_length = 50)
	spename = models.CharField(max_length = 50)
	chrosome = models.CharField(max_length = 30)
	sequence = models.TextField()
	length = models.CharField(max_length = 10)
	def __str__(self):
		return self.name