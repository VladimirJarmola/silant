from django import forms

from deskbook.models import (
    DriveAxle,
    EngineModel,
    FailureNode,
    RecoveryMethod,
    SteeringAxle,
    TransmissionModel,
    VehicleModel,
    ViewMaintenance,
)


class DeskbookBaseForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if VehicleModel.objects.filter(name=name).exists():
            raise forms.ValidationError(
                message="Это имя уже используется!", code="invalid"
            )
        return name


class AddVehicleForm(DeskbookBaseForm):
    class Meta:
        model = VehicleModel
        fields = "__all__"


class AddEngineForm(DeskbookBaseForm):
    class Meta:
        model = EngineModel
        fields = "__all__"


class AddTransmissionForm(DeskbookBaseForm):
    class Meta:
        model = TransmissionModel
        fields = "__all__"


class AddDriveAxleForm(DeskbookBaseForm):
    class Meta:
        model = DriveAxle
        fields = "__all__"


class AddSteeringAxleForm(DeskbookBaseForm):
    class Meta:
        model = SteeringAxle
        fields = "__all__"


class AddFailureNodeForm(DeskbookBaseForm):
    class Meta:
        model = FailureNode
        fields = "__all__"


class AddRecoveryMethodForm(DeskbookBaseForm):
    class Meta:
        model = RecoveryMethod
        fields = "__all__"


class AddViewMaintenanceForm(DeskbookBaseForm):
    class Meta:
        model = ViewMaintenance
        fields = "__all__"
