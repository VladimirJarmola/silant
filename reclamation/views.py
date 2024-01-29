from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from cars.models import Cars

from reclamation.models import Reclamation

# Create your views here.
@login_required
def reclamation(request, failure_node_id=False, recovery_method_id=False, service_company_id=False):

    page = request.GET.get("page", 1)
    ordering = request.GET.get("order_by", None)

    if failure_node_id:
        reclamation_all = Reclamation.objects.filter(failure_node=failure_node_id)
    elif recovery_method_id:
        reclamation_all = Reclamation.objects.filter(recovery_method=recovery_method_id)
    elif service_company_id:
        reclamation_all = Reclamation.objects.filter(service_company__id=service_company_id)
    else:
        reclamation_all = Reclamation.objects.all()

    if ordering and ordering != "default":
        reclamation_all = reclamation_all.order_by(ordering)

    paginator = Paginator(reclamation_all, 5)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Рекламации',
        'reclamation': current_page
    }
    return render(request, 'reclamation/reclamation_all.html', context)


@login_required
def get_reclamation(request, car_id, failure_node_id=False, recovery_method_id=False, service_company_id=False):

    car_item = Cars.objects.get(id=car_id)

    page = request.GET.get('page', 1)
    ordering = request.GET.get("order_by", None)

    if failure_node_id:
        reclamation_list = Reclamation.objects.filter(car__id=car_id).filter(failure_node=failure_node_id)
    elif recovery_method_id:
        reclamation_list = Reclamation.objects.filter(car__id=car_id).filter(recovery_method=recovery_method_id)
    elif service_company_id:
        reclamation_list = Reclamation.objects.filter(car__id=car_id).filter(service_company=service_company_id)    
    else:
        reclamation_list = Reclamation.objects.filter(car__id=car_id)

    failure_node_for_watch = reclamation_list.values_list('failure_node', flat=True)
    recovery_method_for_watch = reclamation_list.values_list('recovery_method', flat=True)
    service_company_for_watch = reclamation_list.values_list('service_company', flat=True)
    
    if ordering and ordering != "default":
        reclamation_list = reclamation_list.order_by(ordering)

    paginator = Paginator(reclamation_list, 2)
    current_page = paginator.page(int(page))

    context = {
        "car": car_item, 
        'reclamations': current_page,
        'fn_for_watch': failure_node_for_watch,
        'rm_for_watch': recovery_method_for_watch,
        'sc_for_watch': service_company_for_watch,
    }

    return render(request, 'reclamation/reclamations.html', context)
