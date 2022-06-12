from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name = 'home'),
path('<slug:car_slug>', views.car, name='car'),

]