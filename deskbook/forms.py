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


class AddVehicleForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if VehicleModel.objects.filter(name=name).exists():
            raise forms.ValidationError(
                message="Это имя уже используется!", code="invalid"
            )
        return name
    
    class Meta:
        model = VehicleModel
        fields = "__all__"


class AddEngineForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if EngineModel.objects.filter(name=name).exists():
            raise forms.ValidationError(
                message="Это имя уже используется!", code="invalid"
            )
        return name
    
    class Meta:
        model = EngineModel
        fields = "__all__"


class AddTransmissionForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if TransmissionModel.objects.filter(name=name).exists():
            raise forms.ValidationError(
                message="Это имя уже используется!", code="invalid"
            )
        return name
    
    class Meta:
        model = TransmissionModel
        fields = "__all__"


class AddDriveAxleForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if DriveAxle.objects.filter(name=name).exists():
            raise forms.ValidationError(
                message="Это имя уже используется!", code="invalid"
            )
        return name
    
    class Meta:
        model = DriveAxle
        fields = "__all__"


class AddSteeringAxleForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if SteeringAxle.objects.filter(name=name).exists():
            raise forms.ValidationError(
                message="Это имя уже используется!", code="invalid"
            )
        return name
    
    class Meta:
        model = SteeringAxle
        fields = "__all__"


class AddFailureNodeForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if FailureNode.objects.filter(name=name).exists():
            raise forms.ValidationError(
                message="Это имя уже используется!", code="invalid"
            )
        return name
    
    class Meta:
        model = FailureNode
        fields = "__all__"


class AddRecoveryMethodForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if RecoveryMethod.objects.filter(name=name).exists():
            raise forms.ValidationError(
                message="Это имя уже используется!", code="invalid"
            )
        return name
    
    class Meta:
        model = RecoveryMethod
        fields = "__all__"


class AddViewMaintenanceForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data["name"]
        if ViewMaintenance.objects.filter(name=name).exists():
            raise forms.ValidationError(
                message="Это имя уже используется!", code="invalid"
            )
        return name
    
    class Meta:
        model = ViewMaintenance
        fields = "__all__"
