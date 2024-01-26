from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

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
    return render(request, 'reclamation/reclamation.html', context)


@login_required
def get_reclamation(request, reclamation_id):
    reclamation_item = Reclamation.objects.get(id=reclamation_id)

    context = {
        "reclamation": reclamation_item, 
    }

    return render(request, 'reclamation/item.html', context)
