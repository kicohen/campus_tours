from django.db import models

# Create your models here.
class Location(models.Model):
	name = models.CharField(max_length=160)
	description = models.TextField(max_length=430, blank=True)
	latitude = models.IntegerField(blank=True, null=True)
	longitude = models.IntegerField(blank=True, null=True)
	image_name = models.CharField(max_length=160)


class Testimonial(models.Model):
	name = models.CharField(max_length=160)
	description = models.TextField(max_length=430, blank=True)
	image_name = models.CharField(max_length=160)
	location = models.ForeignKey(Location)