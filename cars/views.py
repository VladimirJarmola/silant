from django.shortcuts import render
from cars.models import Cars


def cars(request):

    cars_all  = Cars.objects.all().filter(serial_number_vehicle='0017')

    context = {
        'cars': cars_all,
    }

    return render(request, 'cars/cars.html', context)
