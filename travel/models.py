from django.db import models

class Destination(models.Model):
	
	name = models.CharField(max_length=300)
	img = models.ImageField(upload_to ='pics')
	desc = models.TextField()
	price = models.IntegerField()
	offer= models.BooleanField(default=False)

