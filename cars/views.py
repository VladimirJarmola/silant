from django.shortcuts import render
from cars.models import Cars


def cars(request):

    cars  = Cars.objects.all()

    context = {
        'cars': cars,
    }

    return render(request, 'cars/cars.html', context)
