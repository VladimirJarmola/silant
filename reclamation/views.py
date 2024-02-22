import datetime
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from cars.models import Cars
from reclamation.forms import AddReclamationForm
from reclamation.models import Reclamation


@permission_required('reclamation.view_reclamation', raise_exception=True)
def reclamation(request, failure_node_id=False, recovery_method_id=False, service_company_id=False):

    page = request.GET.get("page", 1)
    ordering = request.GET.get("order_by", None)
    user_role = request.user.user_role

    if user_role == 'CL':
        user_cars_list = Cars.objects.filter(client=request.user.id).values_list('id', flat=True)
        reclamation_limited = Reclamation.objects.filter(car__in=user_cars_list)
    elif user_role == 'SE':
        reclamation_limited = Reclamation.objects.filter(service_company=request.user.service_company_id)
    elif user_role == 'MG' or user_role == 'AD':
        reclamation_limited = Reclamation.objects.all()

    failure_node_for_filtration = reclamation_limited.values_list('failure_node', flat=True)
    recovery_method_for_filtration = reclamation_limited.values_list('recovery_method', flat=True)
    service_company_for_filtration = reclamation_limited.values_list('service_company', flat=True)

    if failure_node_id:
        user_reclamation = reclamation_limited.filter(failure_node=failure_node_id)
    elif recovery_method_id:
        user_reclamation = reclamation_limited.filter(recovery_method=recovery_method_id)
    elif service_company_id:
        user_reclamation = reclamation_limited.filter(service_company__id=service_company_id)
    else:
        user_reclamation = reclamation_limited
        
    if ordering and ordering != "default":
        user_reclamation = user_reclamation.order_by(ordering)

    paginator = Paginator(user_reclamation, 5)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Рекламации',
        'reclamation': current_page,
        'fn_filter': failure_node_for_filtration,
        'rm_filter': recovery_method_for_filtration,
        'sc_filter': service_company_for_filtration,
    }
    return render(request, 'reclamation/reclamation_all.html', context)


@permission_required('reclamation.view_reclamation', raise_exception=True)
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
    try:
        current_page = paginator.page(int(page))
    except EmptyPage:
        current_page = paginator.page(int(page) - 1)

    context = {
        "car": car_item, 
        'reclamations': current_page,
        'fn_for_watch': failure_node_for_watch,
        'rm_for_watch': recovery_method_for_watch,
        'sc_for_watch': service_company_for_watch,
    }

    return render(request, 'reclamation/reclamations.html', context)


@permission_required('reclamation.add_reclamation', raise_exception=True)
def add_reclamation(request, car_id=False):
    if request.method == "POST":
        restore_date_introduced = request.POST['restore_date']
        date_of_refusal_introduced = request.POST['date_of_refusal']
        
        if restore_date_introduced <= date_of_refusal_introduced:
            messages.warning(
                request, f"{request.user.username}, дата восстановления должна быть больше даты отказа!"
            )
            return redirect(request.META["HTTP_REFERER"])
        elif datetime.datetime.strptime(restore_date_introduced, '%d.%m.%Y') >= datetime.datetime.today():            
            messages.warning(
                request, f"{request.user.username}, дата восстановления должна быть меньше текущей даты!"
            )
            return redirect(request.META["HTTP_REFERER"])
        
        form = AddReclamationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"{request.user.username}, Вы успешно добавили рекламацию!"
            )
            if not car_id:
                return HttpResponseRedirect(reverse("reclamation:reclamation_all"))
            else:
                return HttpResponseRedirect(reverse("reclamation:car_reclamations", args=(car_id,)))
        else:
            messages.warning(
                request, f"{request.user.username}, Вы неверно ввели данные!"
            )
    elif request.method == "GET" and car_id:
        car = get_object_or_404(Cars, pk=car_id)
        sc_list = Cars.objects.filter(id=car_id).values_list('service_company', flat=True)[0]
        car_list = Cars.objects.filter(id=car_id).values('id')[0]['id']
        form = AddReclamationForm(initial={'car': car_list, 'service_company': sc_list}, car_id=car_id)
    else:
        form = AddReclamationForm()
        car = False

    context = {
        'title': 'Рекламации',
        'form': form,
        'car': car,
    }
    
    return render(request, 'reclamation/add_reclamation.html', context)


@permission_required('reclamation.change_reclamation', raise_exception=True)
def edit_reclamation(request, reclamation_id):
    item = get_object_or_404(Reclamation, id=reclamation_id)
    car_id = item.car.id
    car = get_object_or_404(Cars, id=car_id)

    if request.method == "POST":
        restore_date_introduced = request.POST['restore_date']
        date_of_refusal_introduced = request.POST['date_of_refusal']

        if datetime.datetime.strptime(restore_date_introduced, '%d.%m.%Y') <= datetime.datetime.strptime(date_of_refusal_introduced, '%d.%m.%Y'):
            messages.warning(
                request, f"{request.user.username}, дата восстановления должна быть больше даты отказа!"
            )
            return redirect(request.META["HTTP_REFERER"])
        elif datetime.datetime.strptime(restore_date_introduced, '%d.%m.%Y') >= datetime.datetime.today():            
            messages.warning(
                request, f"{request.user.username}, дата восстановления должна быть меньше текущей даты!"
            )
            return redirect(request.META["HTTP_REFERER"])
        
        form = AddReclamationForm(data=request.POST, instance=item)

        if form.is_valid():
            form.save()
            messages.success(
                request, f"{request.user.username}, Вы успешно изменили рекламацию {item}!"
            )
            return HttpResponseRedirect(reverse("reclamation:car_reclamations", args=(car_id,)))
        else:
            messages.warning(
                request, f"{request.user.username}, Вы неверно ввели данные!"
            )
    else:
        form = AddReclamationForm(instance=item)

    context = {
        'title': 'Рекламации',
        'form': form,
        'item': item,
        'car': car,
    }
    return render(request, 'reclamation/add_reclamation.html', context)


@permission_required('reclamation.delete_reclamation', raise_exception=True)
def remove_reclamation(request, reclamation_id):
    removable = Reclamation.objects.get(id=reclamation_id)
    removable.delete()
    messages.success(
        request, f"{request.user.username}, Вы успешно удалили рекламацию {removable}!"
    )
    try:
        return redirect(request.META["HTTP_REFERER"])
    except EmptyPage:
        return HttpResponseRedirect(reverse("reclamation:reclamation_all"))
