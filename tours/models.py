from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
	name = models.CharField(max_length=160)
	description = models.TextField(max_length=430, blank=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	picture = models.FileField(upload_to="images", blank=True)

	def __str__(self):
		return 'Location: ' + self.name

	def save(self):
		super(Location, self).save()
		if self.picture:
            size = 1667, 1250
            image = Image.open(self.picture)
            image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.picture.name, "w")
            format = 'png'
            image.save(fh, format)
            fh.close()


class Testimonial(models.Model):
	name = models.CharField(max_length=160)
	description = models.TextField(max_length=430, blank=True)
	picture = models.FileField(upload_to="images", blank=True)
	location = models.ForeignKey(Location)

	def __str__(self):
		return 'Testimonial: ' + self.name