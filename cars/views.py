from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from cars.forms import AddCarForm, EditCarForm

from cars.models import Cars

from deskbook.models import VehicleModel

from cars.utils import q_search


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


@login_required
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

    if ordering and ordering != "default":
        cars_all = cars_all.order_by(ordering)

    paginator = Paginator(cars_all, 5)
    try:
        current_page = paginator.page(int(page))
    except EmptyPage:
        current_page = paginator.page(int(page) - 1)

    context = {
        "cars": current_page,
    }

    return render(request, "cars/cars.html", context)


@login_required
def get_car(request, car_id):
    car_item = Cars.objects.get(id=car_id)
    car_vehicle_deskbook = VehicleModel.objects.get(id=car_item.vehicle_model_id)

    context = {"car": car_item, "car_vehicle_deskbook": car_vehicle_deskbook}

    return render(request, "cars/car.html", context)


@login_required
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


@login_required
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


@login_required
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
