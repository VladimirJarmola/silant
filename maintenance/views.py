from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

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
    
    return render(request, "maintenance/maintenance.html", context)


@login_required
def get_maintenance(request, maintenance_id):
    maintenance_item = Maintenance.objects.get(id=maintenance_id)
    # car_vehicle_deskbook = VehicleModel.objects.get(id=car_item.vehicle_model_id)

    context = {
        "maintenance": maintenance_item, 
        # "car_vehicle_deskbook": car_vehicle_deskbook
    }

    return render(request, 'maintenance/item.html', context)
