from django.db import models
from stdimage.models import StdImageField



def download_media_location(instance, filename):
	return "%s" % (filename)

# Create your models here.
class Classes(models.Model):
	title = models.CharField(max_length = 120)
	description = models.TextField(blank=True, null=True)
	image = StdImageField(upload_to=download_media_location, blank=True)
	location = models.CharField(max_length = 200, blank=True, null=True)
	venue = models.CharField(max_length = 200, blank=True, null=True)


	def __str__(self):
		return self.title
