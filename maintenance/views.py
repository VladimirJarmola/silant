from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from cars.models import Cars
from maintenance.forms import AddMaintenanceForm
from maintenance.models import Maintenance


@permission_required('maintenance.view_maintenance', raise_exception=True)
def maintenance(
    request, view_maintenance_id=False, car_id=False, service_company_id=False
):    
    page = request.GET.get("page", 1)
    ordering = request.GET.get("order_by", None)
    user_role = request.user.user_role
    user_cars = Cars.objects.filter(client=request.user.id)

    if user_role == 'CL':
        user_cars_list_id = user_cars.values_list('id', flat=True)
        maintenance_limited = Maintenance.objects.filter(car__in=user_cars_list_id)
    elif user_role == 'SE':
        maintenance_limited = Maintenance.objects.filter(service_company=request.user.service_company_id)
    elif user_role == 'MG' or user_role == 'AD':
        maintenance_limited = Maintenance.objects.all()

    if view_maintenance_id:
        user_maintenance = maintenance_limited.filter(
            view_maintenance=view_maintenance_id
        )
    elif car_id:
        user_maintenance = maintenance_limited.filter(
            car=car_id
        )
    elif service_company_id:
        user_maintenance = maintenance_limited.filter(
            service_company__id=service_company_id
        )
    else:
        user_maintenance = maintenance_limited

    if ordering and ordering != "default":
        user_maintenance = user_maintenance.order_by(ordering)

    paginator = Paginator(user_maintenance, 5)
    current_page = paginator.page(int(page))

    context = {
        "title": "ТО", 
        "maintenance": current_page,
        "serial_number": user_cars,
    }
    
    return render(request, "maintenance/maintenance_all.html", context)


@permission_required('maintenance.view_maintenance', raise_exception=True)
def get_maintenances(request, car_id, view_maintenance_id=False, service_company_id=False):

    page = request.GET.get("page", 1)
    ordering = request.GET.get("order_by", None)

    if view_maintenance_id:
        maintenances_list = Maintenance.objects.filter(car__id=car_id).filter(
            view_maintenance=view_maintenance_id
        )
    elif service_company_id:
        maintenances_list = Maintenance.objects.filter(car__id=car_id).filter(
            service_company=service_company_id
        )
    else:
        maintenances_list = Maintenance.objects.filter(car__id=car_id)

    view_maintenance_for_watch = maintenances_list.values_list('view_maintenance', flat=True)
    service_company_for_watch = maintenances_list.values_list('service_company', flat=True)

    if ordering and ordering != "default":
        maintenances_list = maintenances_list.order_by(ordering)

    car_item = Cars.objects.get(id=car_id)

    paginator = Paginator(maintenances_list, 4)

    try:
        current_page = paginator.page(int(page))
    except EmptyPage:
        current_page = paginator.page(int(page) - 1)
    
    context = {
        "maintenances": current_page, 
        'car': car_item,
        'sc_for_watch': service_company_for_watch,
        'wm_for_watch': view_maintenance_for_watch,
    }

    return render(request, 'maintenance/maintenances.html', context)


@permission_required('maintenance.add_maintenance', raise_exception=True)
def add_maintenance(request, car_id=False):
    if request.method == "POST":
        form = AddMaintenanceForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"{request.user.username}, Вы успешно добавили ТО!"
            )
            if not car_id:
                return HttpResponseRedirect(reverse("maintenance:maintenance_all"))
            else:
                return HttpResponseRedirect(reverse("maintenance:car_maintenances", args=(car_id,)))
        else:
            messages.warning(
                request, f"{request.user.username}, Вы неверно ввели данные!"
            )
    elif request.method == "GET" and car_id:
        car = get_object_or_404(Cars, pk=car_id)
        car_list = Cars.objects.filter(id=car_id).values('id')[0]['id']
        form = AddMaintenanceForm(initial={'car': car_list}, car_id=car_id)
    else:
        form = AddMaintenanceForm()
        car = car_id

    context = {
        'title': 'ТО',
        'form': form,
        'car': car,
    }
    return render(request, 'maintenance/add_maintenance.html', context)


@permission_required('maintenance.change_maintenance', raise_exception=True)
def edit_maintenance(request, view_maintenance_id):
    item = get_object_or_404(Maintenance, id=view_maintenance_id)
    car_id = item.car.id
    if request.method == "POST":
        form = AddMaintenanceForm(data=request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"{request.user.username}, Вы успешно изменили ТО!"
            )
            return HttpResponseRedirect(reverse("maintenance:car_maintenances", args=(car_id,)))
        else:
            messages.warning(
                request, f"{request.user.username}, Вы неверно ввели данные!"
            )
    else:
        form = AddMaintenanceForm(instance=item)

    context = {
        'title': 'ТО',
        'form': form,
        'item': item,
    }
    return render(request, 'maintenance/add_maintenance.html', context)


@permission_required('maintenance.delete_maintenance', raise_exception=True)
def remove_maintenance(request, view_maintenance_id):
    removable = Maintenance.objects.get(id=view_maintenance_id)
    removable.delete()
    messages.success(
        request, f"{request.user.username}, Вы успешно удалили ТО {removable}!"
    )
    try:
        return redirect(request.META["HTTP_REFERER"])
    except EmptyPage:
        return HttpResponseRedirect(reverse("maintenance:maintenance_all"))
