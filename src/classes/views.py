from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import Classes
from products.models import Product

# Create your views here.
class ClassesView(ListView):
	
	model = Classes
	template_name = "classes/list.html"

	def get(self, request, *args, **kwargs):
		context = {}
		classes = Classes.objects.all()
		context["classes"] = classes
		return render(request, self.template_name, context)



class ClassesDetailView(DetailView):
	
	model = Classes
	template_name = "classes/detail.html"

	def get(self, request, *args, **kwargs):
		
		pk = self.kwargs['pk']
		context = {}
		classes = Classes.objects.get(pk=pk)
		products = Product.objects.filter(classes=classes)
		context["class"] = classes
		context["products"] =products
		return render(request, self.template_name, context)