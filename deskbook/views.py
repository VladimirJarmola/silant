from django.contrib import messages
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from deskbook.forms import AddDriveAxleForm, AddEngineForm, AddFailureNodeForm, AddRecoveryMethodForm, AddSteeringAxleForm, AddTransmissionForm, AddVehicleForm, AddViewMaintenanceForm
from deskbook.models import (
    FailureNode,
    RecoveryMethod,
    VehicleModel,
    EngineModel,
    TransmissionModel,
    DriveAxle,
    SteeringAxle,
    ViewMaintenance,
)


def add_deskbook(request, slug):
    if request.method == "GET":
        if slug == "vehicle":
            form = AddVehicleForm()
        elif slug == "engine":
            form = AddEngineForm()
        elif slug == "transmission":
            form = AddTransmissionForm()
        elif slug == "drive_axle":
            form = AddDriveAxleForm()
        elif slug == "steering_axle":
            form = AddSteeringAxleForm()
        elif slug == "failure_node":
            form = AddFailureNodeForm()
        elif slug == "recovery_method":
            form = AddRecoveryMethodForm()
        elif slug == "view_maintenance":
            form = AddViewMaintenanceForm()

    elif request.method == "POST":
        if slug == "vehicle":
            form = AddVehicleForm(data=request.POST)
        elif slug == "engine":
            form = AddEngineForm(data=request.POST)
        elif slug == "transmission":
            form = AddTransmissionForm(data=request.POST)
        elif slug == "drive_axle":
            form = AddDriveAxleForm(data=request.POST)
        elif slug == "steering_axle":
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
                request, f"{request.user.username}, Вы успешно добавили запись!"
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
    }

    return render(request, "deskbook/add_deskbook.html", context=context)


def get_deskbook(request):
    page = request.GET.get("page", 1)

    if "vehicle" in request.path:
        qs = VehicleModel.objects.all()
    elif "engine" in request.path:
        qs = EngineModel.objects.all()
    elif "transmission" in request.path:
        qs = TransmissionModel.objects.all()
    elif "drive_axle" in request.path:
        qs = DriveAxle.objects.all()
    elif "steering_axle" in request.path:
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


def remove_deskbook(request, slug, item_id):

    if slug == "vehicle":
        removable = get_object_or_404(VehicleModel, id=item_id)
    elif slug == "engine":
        removable = get_object_or_404(EngineModel, id=item_id)
    elif slug == "transmission":
        removable = get_object_or_404(TransmissionModel, id=item_id)
    elif slug == "drive_axle":
        removable = get_object_or_404(DriveAxle, id=item_id)
    elif slug == "steering_axle":
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
    

def edit_deskbook(request, slug, item_id):

    if slug == "vehicle":
        item = get_object_or_404(VehicleModel, id=item_id)
    elif slug == "engine":
        item = get_object_or_404(EngineModel, id=item_id)
    elif slug == "transmission":
        item = get_object_or_404(TransmissionModel, id=item_id)
    elif slug == "drive_axle":
        item = get_object_or_404(DriveAxle, id=item_id)
    elif slug == "steering_axle":
        item = get_object_or_404(SteeringAxle, id=item_id)
    elif slug == "failure_node":
        item = get_object_or_404(FailureNode, id=item_id)
    elif slug == "recovery_method":
        item = get_object_or_404(RecoveryMethod, id=item_id)
    elif slug == "view_maintenance":
        item = get_object_or_404(ViewMaintenance, id=item_id)

    if request.method == "GET":
        if slug == "vehicle":
            form = AddVehicleForm(instance=item)
        elif slug == "engine":
            form = AddEngineForm(instance=item)
        elif slug == "transmission":
            form = AddTransmissionForm(instance=item)
        elif slug == "drive_axle":
            form = AddDriveAxleForm(instance=item)
        elif slug == "steering_axle":
            form = AddSteeringAxleForm(instance=item)
        elif slug == "failure_node":
            form = AddFailureNodeForm(instance=item)
        elif slug == "recovery_method":
            form = AddRecoveryMethodForm(instance=item)
        elif slug == "view_maintenance":
            form = AddViewMaintenanceForm(instance=item)

    elif request.method == "POST":
        
        if slug == "vehicle":
            form = AddVehicleForm(data=request.POST, instance=item)
        elif slug == "engine":
            form = AddEngineForm(data=request.POST, instance=item)
        elif slug == "transmission":
            form = AddTransmissionForm(data=request.POST, instance=item)
        elif slug == "drive_axle":
            form = AddDriveAxleForm(data=request.POST, instance=item)
        elif slug == "steering_axle":
            form = AddSteeringAxleForm(data=request.POST, instance=item)
        elif slug == "failure_node":
            form = AddFailureNodeForm(data=request.POST, instance=item)
        elif slug == "recovery_method":
            form = AddRecoveryMethodForm(data=request.POST, instance=item)
        elif slug == "view_maintenance":
            form = AddViewMaintenanceForm(data=request.POST, instance=item)

        if form.is_valid():
            form.save()
            messages.success(
                request, f"{request.user.username}, Вы успешно добавили запись!"
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
