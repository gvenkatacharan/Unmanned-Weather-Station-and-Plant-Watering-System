# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Temperature(models.Model):				#creating a model temperature that can store the temperature values
	tem_value=models.CharField(max_length=250)
	def __str__(self):
		return self.tem_value
class Humidity(models.Model):					#creating a model humidity that can store the humidity values
	hum_value=models.CharField(max_length=250)
	def __str__(self):
		return self.hum_value
class Plant(models.Model):
	plant_id=models.CharField(max_length=250)
	latitude=models.CharField(max_length=250)
	longitude=models.CharField(max_length=250)
	def __str__(self):
		return str(self.plant_id)

class Plantcondition(models.Model):
	plant_id=models.ForeignKey(Plant, on_delete=models.CASCADE,default=0)	
	moi_value=models.CharField(max_length=250)
	actuator_value=models.CharField(max_length=250)
	def __str__(self):
		return str(self.moi_value)
class Waterlevel(models.Model):
	water_value=models.CharField(max_length=250) #creating a model waterlevel that can store the waterlevel values
	def __str__(self):
		return self.water_value
class Watersensor(models.Model):
	water_sensor=models.CharField(max_length=250) #creating a model watersensor that can store the watersensor values
	def __str__(self):
		return self.water_sensor