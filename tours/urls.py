from django.conf.urls import include, url
from tours import views as tours_views

urlpatterns = [
	url(r'^$', tours_views.home, name='home'),
	url(r'^about$', tours_views.about, name='about'),
	url(r'^contact$', tours_views.contact, name='contact'),
	url(r'^destinations$', tours_views.destinations, name='destinations'),
	url(r'^destination$', tours_views.destination, name='destination'),
	url(r'^map$', tours_views.map, name='map'),
]