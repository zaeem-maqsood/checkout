from django.db import models
from stdimage.models import StdImageField



def download_media_location(instance, filename):
	return "%s/%s" % (instance.title, filename)

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length = 120)
	description = models.TextField(blank=True, null=True)
	sale_cost = models.DecimalField(decimal_places = 2, max_digits = 6, null=True, blank=True)
	cost = models.DecimalField(decimal_places = 2, max_digits = 6, null=True, blank=True)
	image = StdImageField(upload_to=download_media_location, blank=True)


	def __str__(self):
		return self.title

