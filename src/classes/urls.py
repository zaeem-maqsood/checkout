from django.conf.urls import url, include

from .views import ClassesView

urlpatterns = [

	url(r'^$', ClassesView.as_view(), name='list'),

]