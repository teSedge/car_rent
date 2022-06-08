from django.db import models
from django.db import models
# Create your models here.

class Car (models.Model):
	name = models.CharField(max_length = 250)
	slug = models.CharField(max_length = 250)
	discription = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'car', blank = True)	
	price = models.IntegerField()
	acceleration = models.FloatField(blank = True, null = True)
	power = models.IntegerField(blank = True, null = True)
	oil = models.CharField(max_length = 250, blank = True, null = True)
	wd = models.CharField(max_length = 250, blank = True, null = True)
	year = models.CharField(max_length = 250, blank = True, null = True)



	def __str__(self):
		return self.name