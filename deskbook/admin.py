from django.contrib import admin

from deskbook.models import VehicleModel, EngineModel, TransmissionModel, DriveAxle, SteeringAxle, FailureNode, RecoveryMethod, ViewMaintenance

# Register your models here.
admin.site.register(VehicleModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DriveAxle)
admin.site.register(SteeringAxle)
admin.site.register(FailureNode)
admin.site.register(RecoveryMethod)
admin.site.register(ViewMaintenance)
