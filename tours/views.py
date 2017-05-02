from django.shortcuts import render, redirect, get_object_or_404, _get_queryset, get_list_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import transaction

from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *

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

def is_logged_in(request):
	if request.user.is_authenticated():
		return True
	return False

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

@login_required
def new_destination(request):
	context = dict()
	if request.method == 'POST':
		form = LocationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return destinations(request)
	context['form'] = LocationForm()
	return render(request, 'tours/new_location.html', context)

################################################################
#                         User Pages                           #
################################################################

@transaction.atomic
def register(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'tours/register.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = RegistrationForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'tours/register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                        password=form.cleaned_data['password1'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    new_user.save()

    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])
    login(request, new_user)
    return redirect(reverse('home'))


################################################################
#                        Debug Pages                           #
################################################################

def clear_session(request):
	request.session.flush()
	return render(request, 'tours/home.html')