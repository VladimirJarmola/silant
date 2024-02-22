from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

from cars.forms import AddCarForm, EditCarForm
from cars.models import Cars
from cars.utils import q_search
from deskbook.models import DriveAxle, EngineModel, SteeringAxle, TransmissionModel, VehicleModel
from maintenance.models import Maintenance
from reclamation.models import Reclamation


def car_search(request):
    query = request.GET.get("q", None)

    if query and len(query.split()):
        car_search_list = q_search(query)
    elif not query:
        messages.warning(request, "Введите заводской номер!")
        return HttpResponseRedirect(reverse("main:index"))
    else:
        car_search_list = None

    # print(car_search_list)
    context = {
        "car_search": car_search_list,
        "content": "По вашему запросу ничего не найдено, данных о машине с таким заводским номером нет в системе",
    }

    return render(request, "cars/car_search.html", context)


@permission_required('cars.view_cars', raise_exception=True)
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
    user_role = request.user.user_role

    if user_role == 'CL':
        cars_limited = Cars.objects.filter(client=request.user.id)
    elif user_role == 'SE':
        cars_limited = Cars.objects.filter(service_company=request.user.service_company_id)
    elif user_role == 'MG' or user_role == 'AD':
        cars_limited = Cars.objects.all()

    vehicle_model_for_filtration = cars_limited.values_list('vehicle_model', flat=True)
    engine_model_for_filtration = cars_limited.values_list('engine_model', flat=True)
    transmission_model_for_filtration = cars_limited.values_list('transmission_model', flat=True)
    drive_axle_model_for_filtration = cars_limited.values_list('drive_axle_model', flat=True)
    steering_axle_model_for_filtration = cars_limited.values_list('steering_axle_model', flat=True)

    
    if vehicle_model_id:
        user_cars = cars_limited.filter(vehicle_model=vehicle_model_id)
    elif engine_model_id:
        user_cars = cars_limited.filter(engine_model=engine_model_id)
    elif transmission_model_id:
        user_cars = cars_limited.filter(transmission_model=transmission_model_id)
    elif drive_axle_model_id:
        user_cars = cars_limited.filter(drive_axle_model=drive_axle_model_id)
    elif steering_axle_model_id:
        user_cars = cars_limited.filter(steering_axle_model=steering_axle_model_id)
    else:
        user_cars = cars_limited

    if ordering and ordering != "default":
        user_cars = user_cars.order_by(ordering)

    paginator = Paginator(user_cars, 5)
    try:
        current_page = paginator.page(int(page))
    except EmptyPage:
        current_page = paginator.page(int(page) - 1)

    context = {
        "cars": current_page,
        'vm_for_filter': vehicle_model_for_filtration,
        'em_for_filter': engine_model_for_filtration,
        'tm_for_filter': transmission_model_for_filtration,
        'dam_for_filter': drive_axle_model_for_filtration,
        'sam_for_filter': steering_axle_model_for_filtration,
    }

    return render(request, "cars/cars.html", context)


@permission_required('cars.add_cars', raise_exception=True)
def add_car(request):
    if request.method == "POST":
        form = AddCarForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"{request.user.username}, Вы успешно добавили машину!"
            )
            return HttpResponseRedirect(reverse("cars:cars"))
        else:
            messages.warning(
                request, f"{request.user.username}, Вы неверно ввели данные!"
            )
    else:
        form = AddCarForm()

    context = {
        "title": "Машины",
        "form": form,
    }
    return render(request, "cars/add_car.html", context)


@permission_required('cars.delete_cars', raise_exception=True)
def remove_car(request, car_id):
    car = Cars.objects.get(id=car_id)
    car.delete()
    messages.success(
        request, f"{request.user.username}, Вы успешно удалили машину {car}!"
    )
    try:
        return redirect(request.META["HTTP_REFERER"])
    except EmptyPage:
        return HttpResponseRedirect(reverse("cars:cars"))


@permission_required('cars.change_cars', raise_exception=True)
def edit_car(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    if request.method == "POST":
        serial_number_vehicle_new = request.POST[
            "serial_number_vehicle"
        ]
        serial_number_of_the_engine_new = request.POST[
            "serial_number_of_the_engine"
        ]
        serial_number_of_the_transmission_new = request.POST[
            "serial_number_of_the_transmission"
        ]
        drive_axle_serial_number_new = request.POST[
            "drive_axle_serial_number"
        ]
        serial_number_of_the_steered_axle_new = request.POST[
            "serial_number_of_the_steered_axle"
        ]

        if (
            car.serial_number_vehicle != serial_number_vehicle_new
            and Cars.objects.filter(
                serial_number_vehicle=serial_number_vehicle_new
            ).exists()
        ):
            messages.warning(
                request, f"{request.user.username}, Указанный номер уже используется!"
            )
            return redirect(request.META["HTTP_REFERER"])
        elif (
            car.serial_number_of_the_engine != serial_number_of_the_engine_new
            and Cars.objects.filter(
                serial_number_of_the_engine=serial_number_of_the_engine_new
            ).exists()
        ):
            messages.warning(
                request, f"{request.user.username}, Указанный номер уже используется!"
            )
            return redirect(request.META["HTTP_REFERER"])
        elif (
            car.serial_number_of_the_transmission
            != serial_number_of_the_transmission_new
            and Cars.objects.filter(
                serial_number_of_the_transmission=serial_number_of_the_transmission_new
            ).exists()
        ):
            messages.warning(
                request, f"{request.user.username}, Указанный номер уже используется!"
            )
            return redirect(request.META["HTTP_REFERER"])
        elif (
            car.drive_axle_serial_number != drive_axle_serial_number_new
            and Cars.objects.filter(
                drive_axle_serial_number=drive_axle_serial_number_new
            ).exists()
        ):
            messages.warning(
                request, f"{request.user.username}, Указанный номер уже используется!"
            )
            return redirect(request.META["HTTP_REFERER"])
        elif (
            car.serial_number_of_the_steered_axle
            != serial_number_of_the_steered_axle_new
            and Cars.objects.filter(
                serial_number_of_the_steered_axle=serial_number_of_the_steered_axle_new
            ).exists()
        ):
            messages.warning(
                request, f"{request.user.username}, Указанный номер уже используется!"
            )
            return redirect(request.META["HTTP_REFERER"])
        else:
            form = EditCarForm(data=request.POST, instance=car)
            if form.is_valid():
                form.save()
                messages.success(
                    request, f"{request.user.username}, Вы успешно изменили машину!"
                )
                return HttpResponseRedirect(reverse("cars:cars"))
            else:
                messages.warning(
                    request, f"{request.user.username}, Вы неверно ввели данные!"
                )
    else:
        form = EditCarForm(instance=car)

    context = {
        "title": "Машины",
        "form": form,
        "car": car,
    }
    return render(request, "cars/add_car.html", context)


@permission_required('cars.view_cars', raise_exception=True)
def car_ajax(request):
    car_id = request.GET.get('car_id')

    car = get_object_or_404(Cars, pk=car_id)
    maintenances = Maintenance.objects.filter(car=car_id)
    reclamations = Reclamation.objects.filter(car=car_id)
    # справочники по машине, описания
    deskbook_for_car = {
        'vehicle_model_description': VehicleModel.objects.get(name=car.vehicle_model).description,
        'engine_model_description': EngineModel.objects.get(name=car.engine_model).description,
        'transmission_model_description': TransmissionModel.objects.get(name=car.transmission_model).description,
        'drive_axle_model_description': DriveAxle.objects.get(name=car.drive_axle_model).description,
        'steering_axle_model_description': SteeringAxle.objects.get(name=car.steering_axle_model).description,
    }
    
    context = {
        'car': car,
        'maintenances': maintenances,
        'reclamations': reclamations,
        'deskbook': deskbook_for_car,
    }

    car_html = render_to_string("includes/modal_car.html", context, request=request)

    response_data = {
        "car_html": car_html,
    }
    
    return JsonResponse(response_data)
