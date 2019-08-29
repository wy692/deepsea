from django.db import models

# Create your models here.
class Lncrna(models.Model):
	name = models.CharField(max_length = 50)
	spename = models.CharField(max_length = 50)
	chrosome = models.CharField(max_length = 30)
	length = models.CharField(max_length = 30)
	sequence = models.TextField()
	def __str__(self):
		return self.name