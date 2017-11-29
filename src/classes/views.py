from django.shortcuts import render
from django.views.generic.list import ListView


from .models import Classes

# Create your views here.
class ClassesView(ListView):
	
	model = Classes
	template_name = "classes/list.html"

	def get(self, request, *args, **kwargs):
		context = {}
		classes = Classes.objects.all()
		context["classes"] = classes
		return render(request, self.template_name, context)