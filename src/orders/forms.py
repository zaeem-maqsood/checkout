from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = [
			"first_name",
			"last_name",
			"email",
			"notes"
		]


		widgets = {
			"first_name": forms.TextInput(
					attrs={
					"required" : True,
					"class":"form-control input",
					"placeholder":"Mohammad"
					}
				),
			"last_name": forms.TextInput(
					attrs={
					"required" : True,
					"class":"form-control input",
					"placeholder":"Ahmed"
					}
				),
			"email": forms.EmailInput(
					attrs={
					"class":"form-control input",
					}
				),
			"notes": forms.Textarea(
					attrs={
					"class":"form-control input",
					}
				),


			}