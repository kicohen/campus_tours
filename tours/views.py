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

@login_required
def admin_panel(request):
	return render(request, 'tours/admin_panel.html')

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

def get_photo(request, id):
    location = get_object_or_404(Location, id=id)
    if not location.picture:
        return
    return HttpResponse(location.picture)

def get_photo_testimonial(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    if not testimonial.picture:
        raise Http404
    return HttpResponse(testimonial.picture)

################################################################
#                       Location Pages                         #
################################################################

def map(request):
	context = dict()
	locations = Location.objects.all()
	context['locations'] = locations
	return render(request, 'tours/map.html', context)

def destination(request):
	visited = request.session.get('visited', [])
	lid = request.GET.get('id', '')
	context = dict()
	location = get_object_or_404(Location, pk=lid)
	testimonials = get_list_or_none(Testimonial, location=location)
	visited.append(location.pk)
	request.session['visited'] = visited
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

@login_required
def list_all(request):
	context = dict()
	context['testimonials'] = Testimonial.objects.all()
	context['locations'] = Location.objects.all()
	return render(request, 'tours/list_all.html', context)

@login_required
def edit_destination(request):
	lid = request.GET.get('id', '')
	context = dict()
	context['edit'] = True
	location = get_object_or_404(Location, pk=lid)
	context['location'] = location
	if request.method == 'POST':
		form = LocationForm(request.POST, request.FILES or None, instance=location)
		if form.is_valid():
			form.save()
			return destinations(request)
	context['form'] = LocationForm(instance=location)
	return render(request, 'tours/new_location.html', context)

@login_required
def delete_destination(request):
	did = request.GET.get('id','')
	destination = get_object_or_404(Location, pk=did)
	destination.delete()
	return list_all(request)

################################################################
#                     Testimonial Pages                        #
################################################################

@login_required
def new_testimonial(request):
	context = dict()
	if request.method == 'POST':
		form = TestimonialForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return list_all(request)
	context['form'] = TestimonialForm()
	return render(request, 'tours/new_testimonial.html', context)


@login_required
def edit_testimonial(request):
	tid = request.GET.get('id', '')
	context = dict()
	context['edit'] = True
	testimonial = get_object_or_404(Testimonial, pk=tid)
	context['testimonial'] = testimonial
	if request.method == 'POST':
		form = TestimonialForm(request.POST, request.FILES or None, instance=testimonial)
		if form.is_valid():
			form.save()
			return list_all(request)
	context['form'] = TestimonialForm(instance=testimonial)
	return render(request, 'tours/new_testimonial.html', context)


@login_required
def delete_testimonial(request):
	tid = request.GET.get('id','')
	testimonial = get_object_or_404(Testimonial, pk=tid)
	testimonial.delete()
	return list_all(request)
	
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