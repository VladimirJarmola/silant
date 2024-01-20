from django.core.paginator import Paginator
from django.shortcuts import render

from cars.models import Cars

from deskbook.models import VehicleModel

from cars.utils import q_search


def car_search(request):

    query = request.GET.get('q', None)
    # car_search_list = []
    # print(query)
    if query:
        car_search_list = q_search(query)
    #     empty = True
    else:
        car_search_list = query
    #     empty = False
    # car_search_item = Cars.objects.all().filter(serial_number_vehicle="0017")
    print(car_search_list)
    context = {
        "car_search": car_search_list,
        "content": 'По вашему запросу ничего не найдено'
        # 'empty': empty,
    }

    return render(request, "cars/car_search.html", context)


def cars(
    request,
    vehicle_model_id=False,
    engine_model_id=False,
    transmission_model_id=False,
    drive_axle_model_id=False,
    steering_axle_model_id=False,
):
    
    page = request.GET.get("page", 1)
    ordering = request.GET.get("order_by", None)

    if vehicle_model_id:
        cars_all = Cars.objects.filter(vehicle_model=vehicle_model_id)
    elif engine_model_id:
        cars_all = Cars.objects.filter(engine_model=engine_model_id)
    elif transmission_model_id:
        cars_all = Cars.objects.filter(transmission_model=transmission_model_id)
    elif drive_axle_model_id:
        cars_all = Cars.objects.filter(drive_axle_model=drive_axle_model_id)
    elif steering_axle_model_id:
        cars_all = Cars.objects.filter(steering_axle_model=steering_axle_model_id)
    else:
        cars_all = Cars.objects.all()

    if ordering and ordering != 'default':
        cars_all = cars_all.order_by(ordering)
    
    paginator = Paginator(cars_all, 5)
    current_page = paginator.page(int(page))

    context = {
        "cars": current_page,
    }

    return render(request, "cars/cars.html", context)


def get_car(request, car_id):
    car_item = Cars.objects.get(id=car_id)
    car_vehicle_deskbook = VehicleModel.objects.get(id=car_item.vehicle_model_id)

    context = {"car": car_item, "car_vehicle_deskbook": car_vehicle_deskbook}

    return render(request, "cars/car.html", context)
