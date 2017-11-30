from django.db import models
from django.core.urlresolvers import reverse

from classes.models import Classes


# Create your models here.
class Product(models.Model):
	classes = models.ForeignKey(Classes)
	title = models.CharField(max_length = 120)
	sale_cost = models.DecimalField(decimal_places = 2, max_digits = 6, null=True, blank=True)
	cost = models.DecimalField(decimal_places = 2, max_digits = 6, null=True, blank=True)
	instructor = models.CharField(max_length = 120, null=True, blank=True)
	interval = models.CharField(max_length = 50)
	feature1 = models.CharField(max_length = 120, null=True, blank=True)
	feature2 = models.CharField(max_length = 120, null=True, blank=True)
	feature3 = models.CharField(max_length = 120, null=True, blank=True)
	feature4 = models.CharField(max_length = 120, null=True, blank=True)
	feature5 = models.CharField(max_length = 120, null=True, blank=True)
	feature6 = models.CharField(max_length = 120, null=True, blank=True)
	checkout_instructions = models.TextField(blank=True, null=True)
	button_text = models.CharField(max_length = 50)



	def __str__(self):
		return self.title


	def get_absolute_url(self):
		view_name = "products:detail"
		return reverse(view_name, kwargs={"pk": self.pk})
