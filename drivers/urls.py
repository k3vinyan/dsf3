from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^roster/', views.roster, name='roster'),
    #url(r'^addDrivers/', views.addDrivers, name='addDrivers'),
]