from django.conf.urls import include, url
from tours import views as tours_views

urlpatterns = [
	url(r'^$', tours_views.home, name='home'),
]