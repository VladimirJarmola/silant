from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from cars.models import Cars
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
            car__vehicle_model=car_id
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
    current_page = paginator.page(int(page))

    context = {
        "maintenances": current_page, 
        'car': car_item,
        'sc_for_watch': service_company_for_watch,
        'wm_for_watch': view_maintenance_for_watch,
    }

    return render(request, 'maintenance/maintenances.html', context)
