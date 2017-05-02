from django.shortcuts import render, redirect, get_object_or_404, _get_queryset, get_list_or_404
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

################################################################
#                         Static Pages                         #
################################################################

def home(request):
	return render(request, 'tours/home.html')

def about(request):
	return render(request, 'tours/about.html')

def contact(request):
	return render(request, 'tours/contact.html')

################################################################
#                       Helper Functions                       #
################################################################

def get_list_or_none(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    obj_list = list(queryset.filter(*args, **kwargs))
    if not obj_list:
        return None
    return obj_list

################################################################
#                       Location Pages                         #
################################################################

def map(request):
	context = dict()
	locations = Location.objects.all()
	context['locations'] = locations
	return render(request, 'tours/map.html', context)

def destination(request):
	if 'visited' not in request.session:
		print('Visited in session')
		request.session['visited'] = []
	lid = request.GET.get('id', '')
	context = dict()
	location = get_object_or_404(Location, pk=lid)
	testimonials = get_list_or_none(Testimonial, location=location)
	request.session['visited'].append(location.pk)
	context['location'] = location
	context['testimonials'] = testimonials
	return render(request, 'tours/destination.html', context)

def destinations(request):
	context = dict()
	locations = Location.objects.all()
	context['locations'] = locations
	return render(request, 'tours/list.html', context)


################################################################
#                        Debug Pages                           #
################################################################

def clear_session(request):
	request.session.flush()
	return render(request, 'tours/home.html')