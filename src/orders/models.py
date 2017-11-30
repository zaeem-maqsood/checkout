from django.db import models

from products.models import Product

# Create your models here.
class Order(models.Model):
	product = models.ForeignKey(Product)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	first_name = models.CharField(max_length = 120)
	last_name = models.CharField(max_length = 120)
	email = models.EmailField(max_length=254)
	notes = models.TextField(null=True)
	charge_id = models.CharField(max_length=200, null=True, blank=True) 

	def __str__(self):
		return self.first_name