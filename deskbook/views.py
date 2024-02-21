from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse

from deskbook.forms import (
    AddServiceCompany,
    AddDriveAxleForm,
    AddEngineForm,
    AddFailureNodeForm,
    AddRecoveryMethodForm,
    AddSteeringAxleForm,
    AddTransmissionForm,
    AddVehicleForm,
    AddViewMaintenanceForm,
)
from deskbook.forms import (
    EditServiceCompany,
    EditDriveAxleForm,
    EditEngineForm,
    EditFailureNodeForm,
    EditRecoveryMethodForm,
    EditSteeringAxleForm,
    EditTransmissionForm,
    EditVehicleForm,
    EditViewMaintenanceForm,
)
from deskbook.models import (
    ServiceCompany,
    FailureNode,
    RecoveryMethod,
    VehicleModel,
    EngineModel,
    TransmissionModel,
    DriveAxle,
    SteeringAxle,
    ViewMaintenance,
)


@login_required
def add_deskbook(request, slug):
    deskbook_add_permission = [f'deskbook.{el}' for el in Permission.objects.filter(
        content_type__app_label="deskbook", codename__startswith="add"
    ).values_list("codename", flat=True)]
    
    if not request.user.has_perms(deskbook_add_permission):
        raise PermissionDenied
    
    if request.method == "GET":
        path = request.META["HTTP_REFERER"]
        if slug == "service_company":
            form = AddServiceCompany()
        elif slug == "vehicle_model":
            form = AddVehicleForm()
        elif slug == "engine_model":
            form = AddEngineForm()
        elif slug == "transmission_model":
            form = AddTransmissionForm()
        elif slug == "drive_axle_model":
            form = AddDriveAxleForm()
        elif slug == "steering_axle_model":
            form = AddSteeringAxleForm()
        elif slug == "failure_node":
            form = AddFailureNodeForm()
        elif slug == "recovery_method":
            form = AddRecoveryMethodForm()
        elif slug == "view_maintenance":
            form = AddViewMaintenanceForm()

    elif request.method == "POST":
        path = request.POST.get("path_referer", None)
        if slug == "service_company":
            form = AddServiceCompany(data=request.POST)
        elif slug == "vehicle_model":
            form = AddVehicleForm(data=request.POST)
        elif slug == "engine_model":
            form = AddEngineForm(data=request.POST)
        elif slug == "transmission_model":
            form = AddTransmissionForm(data=request.POST)
        elif slug == "drive_axle_model":
            form = AddDriveAxleForm(data=request.POST)
        elif slug == "steering_axle_model":
            form = AddSteeringAxleForm(data=request.POST)
        elif slug == "failure_node":
            form = AddFailureNodeForm(data=request.POST)
        elif slug == "recovery_method":
            form = AddRecoveryMethodForm(data=request.POST)
        elif slug == "view_maintenance":
            form = AddViewMaintenanceForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"{request.user.username}, Вы успешно добавили запись в справочник!",
            )
            if path:
                return HttpResponseRedirect(path)
            else:
                return HttpResponseRedirect(reverse(f"deskbook:{slug}"))
        else:
            messages.warning(
                request, f"{request.user.username}, Вы неверно ввели данные!"
            )

    context = {
        "title": "Справочники",
        "form": form,
        "slug": slug,
        "path": path,
    }

    return render(request, "deskbook/add_deskbook.html", context=context)


@login_required
def get_deskbook(request):
    deskbook_view_permission = [f'deskbook.{el}' for el in Permission.objects.filter(
        content_type__app_label="deskbook", codename__startswith="view"
    ).values_list("codename", flat=True)]
    
    if not request.user.has_perms(deskbook_view_permission) or not request.user.user_role in ['MG', 'AD']:
        raise PermissionDenied
    
    page = request.GET.get("page", 1)

    if "service_company" in request.path:
        qs = ServiceCompany.objects.all()
    elif "vehicle_model" in request.path:
        qs = VehicleModel.objects.all()
    elif "engine_model" in request.path:
        qs = EngineModel.objects.all()
    elif "transmission_model" in request.path:
        qs = TransmissionModel.objects.all()
    elif "drive_axle_model" in request.path:
        qs = DriveAxle.objects.all()
    elif "steering_axle_model" in request.path:
        qs = SteeringAxle.objects.all()
    elif "failure_node" in request.path:
        qs = FailureNode.objects.all()
    elif "recovery_method" in request.path:
        qs = RecoveryMethod.objects.all()
    elif "view_maintenance" in request.path:
        qs = ViewMaintenance.objects.all()

    paginator = Paginator(qs, 5)

    try:
        current_page = paginator.page(int(page))
    except EmptyPage:
        current_page = paginator.page(int(page) - 1)

    context = {
        "title": "Справочники",
        "deskbook": current_page,
    }

    return render(request, "deskbook/deskbook.html", context=context)


@login_required
def remove_deskbook(request, slug, item_id):
    deskbook_delete_permission = [f'deskbook.{el}' for el in Permission.objects.filter(
        content_type__app_label="deskbook", codename__startswith="delete"
    ).values_list("codename", flat=True)]

    if not request.user.has_perms(deskbook_delete_permission):
        raise PermissionDenied
    
    if slug == "service_company":
        removable = get_object_or_404(ServiceCompany, id=item_id)
    elif slug == "vehicle_model":
        removable = get_object_or_404(VehicleModel, id=item_id)
    elif slug == "engine_model":
        removable = get_object_or_404(EngineModel, id=item_id)
    elif slug == "transmission_model":
        removable = get_object_or_404(TransmissionModel, id=item_id)
    elif slug == "drive_axle_model":
        removable = get_object_or_404(DriveAxle, id=item_id)
    elif slug == "steering_axle_model":
        removable = get_object_or_404(SteeringAxle, id=item_id)
    elif slug == "failure_node":
        removable = get_object_or_404(FailureNode, id=item_id)
    elif slug == "recovery_method":
        removable = get_object_or_404(RecoveryMethod, id=item_id)
    elif slug == "view_maintenance":
        removable = get_object_or_404(ViewMaintenance, id=item_id)

    removable.delete()

    try:
        return redirect(request.META["HTTP_REFERER"])
    except EmptyPage:
        return HttpResponseRedirect(reverse(f"deskbook:{slug}"))


@login_required
def edit_deskbook(request, slug, item_id):
    deskbook_change_permission = [f'deskbook.{el}' for el in Permission.objects.filter(
        content_type__app_label="deskbook", codename__startswith="change"
     ).values_list("codename", flat=True)]
    
    if not request.user.has_perms(deskbook_change_permission):
        raise PermissionDenied
    
    if slug == "service_company":
        item = get_object_or_404(ServiceCompany, id=item_id)
    elif slug == "vehicle_model":
        item = get_object_or_404(VehicleModel, id=item_id)
    elif slug == "engine_model":
        item = get_object_or_404(EngineModel, id=item_id)
    elif slug == "transmission_model":
        item = get_object_or_404(TransmissionModel, id=item_id)
    elif slug == "drive_axle_model":
        item = get_object_or_404(DriveAxle, id=item_id)
    elif slug == "steering_axle_model":
        item = get_object_or_404(SteeringAxle, id=item_id)
    elif slug == "failure_node":
        item = get_object_or_404(FailureNode, id=item_id)
    elif slug == "recovery_method":
        item = get_object_or_404(RecoveryMethod, id=item_id)
    elif slug == "view_maintenance":
        item = get_object_or_404(ViewMaintenance, id=item_id)

    if request.method == "GET":
        if slug == "service_company":
            form = EditServiceCompany(instance=item)
        elif slug == "vehicle_model":
            form = EditVehicleForm(instance=item)
        elif slug == "engine_model":
            form = EditEngineForm(instance=item)
        elif slug == "transmission_model":
            form = EditTransmissionForm(instance=item)
        elif slug == "drive_axle_model":
            form = EditDriveAxleForm(instance=item)
        elif slug == "steering_axle_model":
            form = EditSteeringAxleForm(instance=item)
        elif slug == "failure_node":
            form = EditFailureNodeForm(instance=item)
        elif slug == "recovery_method":
            form = EditRecoveryMethodForm(instance=item)
        elif slug == "view_maintenance":
            form = EditViewMaintenanceForm(instance=item)

    elif request.method == "POST":
        if slug == "service_company":
            form = EditServiceCompany(data=request.POST, instance=item)
        elif slug == "vehicle_model":
            form = EditVehicleForm(data=request.POST, instance=item)
        elif slug == "engine_model":
            form = EditEngineForm(data=request.POST, instance=item)
        elif slug == "transmission_model":
            form = EditTransmissionForm(data=request.POST, instance=item)
        elif slug == "drive_axle_model":
            form = EditDriveAxleForm(data=request.POST, instance=item)
        elif slug == "steering_axle_model":
            form = EditSteeringAxleForm(data=request.POST, instance=item)
        elif slug == "failure_node":
            form = EditFailureNodeForm(data=request.POST, instance=item)
        elif slug == "recovery_method":
            form = EditRecoveryMethodForm(data=request.POST, instance=item)
        elif slug == "view_maintenance":
            form = EditViewMaintenanceForm(data=request.POST, instance=item)

        if form.is_valid():
            form.save()
            messages.success(
                request, f"{request.user.username}, Вы успешно изменили запись!"
            )
            return HttpResponseRedirect(reverse(f"deskbook:{slug}"))
        else:
            messages.warning(
                request, f"{request.user.username}, Вы неверно ввели данные!"
            )

    context = {
        "title": "Справочники",
        "form": form,
        "slug": slug,
        "item_id": item_id,
    }

    return render(request, "deskbook/add_deskbook.html", context=context)


@login_required
def deskbook_ajax(request):
    deskbook_view_permission = [f'deskbook.{el}' for el in Permission.objects.filter(
        content_type__app_label="deskbook", codename__startswith="view"
    ).values_list("codename", flat=True)]
    
    if not request.user.has_perms(deskbook_view_permission):
        raise PermissionDenied

    item_id = request.GET.get("deskbook_id")
    slug = request.GET.get("deskbook_name")

    if slug == "service_company":
        item = get_object_or_404(ServiceCompany, id=item_id)
    elif slug == "vehicle_model":
        item = get_object_or_404(VehicleModel, id=item_id)
    elif slug == "engine_model":
        item = get_object_or_404(EngineModel, id=item_id)
    elif slug == "transmission_model":
        item = get_object_or_404(TransmissionModel, id=item_id)
    elif slug == "drive_axle_model":
        item = get_object_or_404(DriveAxle, id=item_id)
    elif slug == "steering_axle_model":
        item = get_object_or_404(SteeringAxle, id=item_id)
    elif slug == "failure_node":
        item = get_object_or_404(FailureNode, id=item_id)
    elif slug == "recovery_method":
        item = get_object_or_404(RecoveryMethod, id=item_id)
    elif slug == "view_maintenance":
        item = get_object_or_404(ViewMaintenance, id=item_id)

    context = {
        "item": item,
    }

    item_html = render_to_string(
        "includes/modal_deskbook.html", context, request=request
    )

    response_data = {
        # "message": "ответ",
        "item_html": item_html,
    }

    return JsonResponse(response_data)
