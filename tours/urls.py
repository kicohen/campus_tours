from django.conf.urls import include, url
from tours import views as tours_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', tours_views.home, name='home'),
	url(r'^about$', tours_views.about, name='about'),
	url(r'^contact$', tours_views.contact, name='contact'),
	url(r'^destinations$', tours_views.destinations, name='destinations'),
	url(r'^destination$', tours_views.destination, name='destination'),
	url(r'^destination/edit$', tours_views.edit_destination, name='edit_destination'),
	url(r'^testimonial/edit$', tours_views.edit_testimonial, name='edit_testimonial'),
	url(r'^destination/delete$', tours_views.delete_destination, name='delete_destination'),
	url(r'^testimonial/delete$', tours_views.delete_testimonial, name='delete_testimonial'),
	url(r'^new_destination$', tours_views.new_destination, name='new_destination'),
	url(r'^new_testimonial$', tours_views.new_testimonial, name='new_testimonial'),
	url(r'^map$', tours_views.map, name='map'),
	url(r'^flush$', tours_views.clear_session, name='flush'),
	url(r'^register$', tours_views.register, name='register'),
	url(r'^login$', auth_views.login, {'template_name':'tours/login.html'}, name='login'),
    url(r'^logout/$',auth_views.logout, {'next_page':'login'}, name='logout'),
    url(r'^admin_panel$', tours_views.admin_panel, name='admin_panel'),
    url(r'^list_all$', tours_views.list_all, name='list_all'),
    url(r'^photo/(?P<id>\d+)$', tours_views.get_photo, name='photo'),
    url(r'^photo_testimonial/(?P<id>\d+)$', tours_views.get_photo_testimonial, name='photo_testimonial'),
]