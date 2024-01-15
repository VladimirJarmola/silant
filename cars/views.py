from django.shortcuts import render
from cars.models import Cars


def car_search(request):

    car_search  = Cars.objects.all().filter(serial_number_vehicle='0017')

    context = {
        'car_search': car_search,
    }

    return render(request, 'cars/car.html', context)


def cars(request):

    cars_all  = Cars.objects.all()

    context = {
        'cars': cars_all,
    }

    return render(request, 'cars/cars.html', context)