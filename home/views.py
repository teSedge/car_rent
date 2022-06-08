from django.shortcuts import render

# Create your views here.

def home (request):
	return render(request, 'home.html')

def car (request):
	return render(request, 'car_page.html')	