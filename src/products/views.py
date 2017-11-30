from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
import stripe
from django.utils import timezone

from .models import Product
from orders.forms import OrderForm
# Create your views here.

class ProductView(FormView):
	
	model = Product
	template_name = "products/checkout.html"
	form_class = OrderForm

	def get_success_url(self):
		return reverse('class:list')

	def get(self, request, *args, **kwargs):
		return self.render_to_response(self.get_context_data(request=request))

	def post(self, request, *args, **kwargs):

		self.object = None
		form = self.get_form()
		pk = self.kwargs['pk']
		product = Product.objects.get(pk=pk)
		nonce = request.POST.get("stripeToken")

		if form.is_valid():
			return self.form_valid(form, nonce, request, product)
		else:
			return self.form_invalid(form, request)


	def form_valid(self, form, nonce, request, product):

		form.instance.created_time = timezone.now()
		form.instance.product = product

		if product.sale_cost:
			total = product.sale_cost
		else:
			total = product.cost
		
		print(nonce)
		if nonce:
			try:
				stripe.api_key = settings.STRIPE_SECRET_KEY
				result = stripe.Charge.create(
						amount = int(total * 100),
						currency = "cad",
						card= nonce,
						description= "Ilm Academy \nClass: %s \nProduct: %s \nNotes: %s" % (product.classes, product.title),
					)
			except Exception as e:
				messages.error(request, "There was a problem with your payment card. Please try another one.")
				return redirect(product.get_absolute_url())
				print(e)

		print(result)
		form.instance.charge_id = result.id
		self.object = form.save()
		messages.success(request, "Congratulations, your order is complete. Please check you email.")
		valid_data = super(ProductView, self).form_valid(form)
		return valid_data


	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))


	def get_context_data(self, request, *args, **kwargs):
		pk = self.kwargs['pk']
		form = self.get_form_class()
		product = Product.objects.get(pk=pk)
		context = {}

		if product.sale_cost:
			total = product.sale_cost
		else:
			total = product.cost

		context["product"] = product
		context["form"] = form
		context["public_key"] = settings.STRIPE_PUBLIC_KEY
		context["total"] = total
		context["stripe_total"] = total * 100
		return context











