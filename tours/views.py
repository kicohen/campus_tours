from django.shortcuts import render, redirect, get_object_or_404, _get_queryset, get_list_or_404

# Create your views here.
def home(request):
	return render(request, 'tours/home.html')

def about(request):
	return render(request, 'tours/about.html')

def contact(request):
	return render(request, 'tours/contact.html')

def map(request):
	return render(request, 'tours/map.html')

def destination(request):
	return render(request, 'tours/destination.html')

def destinations(request):
	return render(request, 'tours/list.html')