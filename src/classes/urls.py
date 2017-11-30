from django.conf.urls import url, include

from .views import ClassesView, ClassesDetailView

urlpatterns = [

	url(r'^$', ClassesView.as_view(), name='list'),
	url(r'^(?P<pk>\d+)/$', ClassesDetailView.as_view(), name='detail'),

]