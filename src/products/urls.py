from django.conf.urls import url, include

from .views import ProductsView

urlpatterns = [

	url(r'^$', ProductsView.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)/$', EventDetailView.as_view(), name='detail'),

]