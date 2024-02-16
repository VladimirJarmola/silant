from django.contrib import admin

from deskbook.models import (
    VehicleModel,
    EngineModel,
    TransmissionModel,
    DriveAxle,
    SteeringAxle,
    FailureNode,
    RecoveryMethod,
    ViewMaintenance,
    ServiceCompany
)


@admin.register(ServiceCompany)
class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['description']
    search_fields = ['name', 'description']

@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['description']
    search_fields = ['name', 'description']


@admin.register(EngineModel)
class EngineModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['description']
    search_fields = ['name', 'description']


@admin.register(TransmissionModel)
class TransmissionModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['description']
    search_fields = ['name', 'description']


@admin.register(DriveAxle)
class DriveAxleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['description']
    search_fields = ['name', 'description']


@admin.register(SteeringAxle)
class SteeringAxleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['description']
    search_fields = ['name', 'description']


@admin.register(FailureNode)
class FailureNodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['description']
    search_fields = ['name', 'description']


@admin.register(RecoveryMethod)
class RecoveryMethodAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['description']
    search_fields = ['name', 'description']


@admin.register(ViewMaintenance)
class ViewMaintenanceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['description']
    search_fields = ['name', 'description']
