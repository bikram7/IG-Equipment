from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^item(?P<pk>\d)', views.item, name='item'), 
]
