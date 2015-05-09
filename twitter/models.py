from django.db import models

# users: anombela password: anombela

# Create your models here.

class Persona(models.Model):
	name = models.CharField(max_length=32)

class Tweet(models.Model):
	content = models.CharField(max_length=150)
	url = models.CharField(max_length=64)
	name = models.ForeignKey(Persona)

