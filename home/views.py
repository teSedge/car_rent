from django.shortcuts import render
from .models import Car, Car_secondary_img

# Create your views here.

def home (request):
	cars = Car.objects.all()
	return render(request, 'home.html', {'cars':cars})

def car (request, car_slug):
	try:
		car = Car.objects.get(slug = car_slug)
		imgs = Car_secondary_img.objects.all().filter(car = car)
	except Exception as e:
		raise e
	return render(request, 'car_page.html',{'car':car,'imgs':imgs})
