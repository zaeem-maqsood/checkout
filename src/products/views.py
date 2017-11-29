from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Product
# Create your views here.

class ProductsView(ListView):
	
	model = Product
	template_name = "products/list.html"

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, self.template_name, context)