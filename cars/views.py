from django.core.paginator import Paginator
from django.shortcuts import render

from cars.models import Cars

from deskbook.models import VehicleModel


def car_search(request):

    car_search  = Cars.objects.all().filter(serial_number_vehicle='0017')

    context = {
        'car_search': car_search,
    }

    return render(request, 'cars/car_search.html', context)


def cars(request):

    page = request.GET.get('page', 1)

    cars_all  = Cars.objects.all()

    paginator = Paginator(cars_all, 2)
    current_page = paginator.page(int(page))

    context = {
        'cars': current_page,
    }

    return render(request, 'cars/cars.html', context)


def get_car(request, car_id):

    car_item  = Cars.objects.get(id=car_id)
    car_vehicle_deskbook = VehicleModel.objects.get(id=car_item.vehicle_model_id)

    context = {
        'car': car_item,
        'car_vehicle_deskbook': car_vehicle_deskbook
    }

    return render(request, 'cars/car.html', context)
