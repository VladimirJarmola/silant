from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from cars.models import Cars
from maintenance.forms import AddMaintenanceForm
from maintenance.models import Maintenance


# Create your views here.
@login_required
def maintenance(
    request, view_maintenance_id=False, car_id=False, service_company_id=False
):
    
    page = request.GET.get("page", 1)
    ordering = request.GET.get("order_by", None)

    if view_maintenance_id:
        maintenance_all = Maintenance.objects.filter(
            view_maintenance=view_maintenance_id
        )
    elif car_id:
        maintenance_all = Maintenance.objects.filter(
            car=car_id
        )
    elif service_company_id:
        maintenance_all = Maintenance.objects.filter(
            service_company__id=service_company_id
        )
    else:
        maintenance_all = Maintenance.objects.all()

    if ordering and ordering != "default":
        maintenance_all = maintenance_all.order_by(ordering)

    paginator = Paginator(maintenance_all, 5)
    current_page = paginator.page(int(page))

    context = {
        "title": "ТО", 
        "maintenance": current_page
    }
    
    return render(request, "maintenance/maintenance_all.html", context)


@login_required
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


@login_required
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

    context = {
        'title': 'ТО',
        'form': form,
        'car': car,
    }
    return render(request, 'maintenance/add_maintenance.html', context)

@login_required
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

@login_required
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
