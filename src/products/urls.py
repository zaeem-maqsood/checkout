from django.conf.urls import url, include

from .views import ProductView

urlpatterns = [

    url(r'^checkout/(?P<pk>\d+)/$', ProductView.as_view(), name='detail'),

]