from django import forms

from cars.models import Cars
from deskbook.models import (
    ServiceCompany,
    DriveAxle,
    EngineModel,
    SteeringAxle,
    TransmissionModel,
    VehicleModel,
)
from users.models import User


class AddCarForm(forms.ModelForm):

    def clean_serial_number_vehicle(self):
        number = self.cleaned_data["serial_number_vehicle"]
        if Cars.objects.filter(serial_number_vehicle=number).exists():
            raise forms.ValidationError(
                message="Этот номер уже используется!", code="invalid"
            )
        elif len(str(number)) != 4:
            raise forms.ValidationError(
                message="Номер должен состоять из 4х цифр!", code="invalid"
            )
        for numb in number:
            if not numb.isdigit():
                raise forms.ValidationError(
                message="Номер должен состоять из цифр!", code="invalid"
            )
        return number

    def clean_serial_number_of_the_engine(self):
        number = self.cleaned_data["serial_number_of_the_engine"]
        if Cars.objects.filter(serial_number_of_the_engine=number).exists():
            raise forms.ValidationError(
                message="Этот номер уже используется!", code="invalid"
            )
        return number

    def clean_serial_number_of_the_transmission(self):
        number = self.cleaned_data["serial_number_of_the_transmission"]
        if Cars.objects.filter(serial_number_of_the_transmission=number).exists():
            raise forms.ValidationError(
                message="Этот номер уже используется!", code="invalid"
            )
        return number

    def clean_drive_axle_serial_number(self):
        number = self.cleaned_data["drive_axle_serial_number"]
        if Cars.objects.filter(drive_axle_serial_number=number).exists():
            raise forms.ValidationError(
                message="Этот номер уже используется!", code="invalid"
            )
        return number

    def serial_number_of_the_steered_axle(self):
        number = self.cleaned_data["serial_number_of_the_steered_axle"]
        if Cars.objects.filter(serial_number_of_the_steered_axle=number).exists():
            raise forms.ValidationError(
                message="Этот номер уже используется!", code="invalid"
            )
        return number

    class Meta:
        model = Cars
        fields = "__all__"
        # exclude = ['client',]

    serial_number_vehicle = forms.CharField(
        label="Заводской номер машины: ",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Укажите номер",
                "class": "form-control auth-width",
            }
        ),
    )

    vehicle_model = forms.ModelChoiceField(
        queryset=VehicleModel.objects.all(),
        label="Модель техники: ",
        empty_label="Выберите модель",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    engine_model = forms.ModelChoiceField(
        queryset=EngineModel.objects.all(),
        label="Модель двигателя: ",
        empty_label="Выберите модель",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    serial_number_of_the_engine = forms.CharField(
        label="Заводской номер двигателя: ",
        widget=forms.TextInput(
            attrs={"placeholder": "Укажите номер", "class": "form-control auth-width"}
        ),
    )

    transmission_model = forms.ModelChoiceField(
        queryset=TransmissionModel.objects.all(),
        label="Модель трансмиссии: ",
        empty_label="Выберите модель",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    serial_number_of_the_transmission = forms.CharField(
        label="Заводской номер трансмиссии: ",
        widget=forms.TextInput(
            attrs={"placeholder": "Укажите номер", "class": "form-control auth-width"}
        ),
    )

    drive_axle_model = forms.ModelChoiceField(
        queryset=DriveAxle.objects.all(),
        label="Модель ведущего моста: ",
        empty_label="Выберите модель",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    drive_axle_serial_number = forms.CharField(
        label="Заводской номер ведущего моста: ",
        widget=forms.TextInput(
            attrs={"placeholder": "Укажите номер", "class": "form-control auth-width"}
        ),
    )

    steering_axle_model = forms.ModelChoiceField(
        queryset=SteeringAxle.objects.all(),
        label="Модель управляемого моста: ",
        empty_label="Выберите модель",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    serial_number_of_the_steered_axle = forms.CharField(
        label="Заводской номер управляемого моста: ",
        widget=forms.TextInput(
            attrs={"placeholder": "Укажите номер", "class": "form-control auth-width"}
        ),
    )

    supply_contract = forms.CharField(
        label="Номер и дата договора поставки: ",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Укажите номер и дату",
                "class": "form-control auth-width",
            }
        ),
    )

    date_shipped_from_factory = forms.DateField(
        label="Дата отгрузки с завода: ",
        widget=forms.DateInput(
            attrs={"placeholder": "Укажите дату", "class": "form-control auth-width"}
        ),
    )

    consignee = forms.CharField(
        label="Грузополучатель (конечный потребитель): ",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Укажите грузополучателя",
                "class": "form-control auth-width",
            }
        ),
    )

    delivery_address = forms.CharField(
        label="Адрес поставки (эксплуатации): ",
        widget=forms.TextInput(
            attrs={"placeholder": "Укажите адрес", "class": "form-control auth-width"}
        ),
    )

    equipment = forms.CharField(
        label="Комплектация (дополнительные опции): ",
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Введите текст", "class": "form-control auth-width"}
        ),
    )

    client = forms.ModelChoiceField(
        queryset=User.objects.all().filter(user_role="CL"),
        label="Клиент: ",
        empty_label="Выберите клиента",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    service_company = forms.ModelChoiceField(
        queryset=ServiceCompany.objects.all(),
        label="Сервисная компания: ",
        empty_label="Выберите компанию",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

class EditCarForm(forms.ModelForm):

    def clean_serial_number_vehicle(self):
        
        number = self.cleaned_data["serial_number_vehicle"]

        if len(str(number)) != 4:
            raise forms.ValidationError(
                message="Номер должен состоять из 4х цифр!", code="invalid"
            )
        for numb in number:
            if not numb.isdigit():
                raise forms.ValidationError(
                message="Номер должен состоять из цифр!", code="invalid"
            )
        return number


    class Meta:
        model = Cars
        fields = "__all__"
        # exclude = ['client',]

    serial_number_vehicle = forms.CharField(
        label="Заводской номер машины: ",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Укажите номер",
                "class": "form-control auth-width",
            }
        ),
    )

    vehicle_model = forms.ModelChoiceField(
        queryset=VehicleModel.objects.all(),
        label="Модель техники: ",
        empty_label="Выберите модель",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    engine_model = forms.ModelChoiceField(
        queryset=EngineModel.objects.all(),
        label="Модель двигателя: ",
        empty_label="Выберите модель",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    serial_number_of_the_engine = forms.CharField(
        label="Заводской номер двигателя: ",
        widget=forms.TextInput(
            attrs={"placeholder": "Укажите номер", "class": "form-control auth-width"}
        ),
    )

    transmission_model = forms.ModelChoiceField(
        queryset=TransmissionModel.objects.all(),
        label="Модель трансмиссии: ",
        empty_label="Выберите модель",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    serial_number_of_the_transmission = forms.CharField(
        label="Заводской номер трансмиссии: ",
        widget=forms.TextInput(
            attrs={"placeholder": "Укажите номер", "class": "form-control auth-width"}
        ),
    )

    drive_axle_model = forms.ModelChoiceField(
        queryset=DriveAxle.objects.all(),
        label="Модель ведущего моста: ",
        empty_label="Выберите модель",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    drive_axle_serial_number = forms.CharField(
        label="Заводской номер ведущего моста: ",
        widget=forms.TextInput(
            attrs={"placeholder": "Укажите номер", "class": "form-control auth-width"}
        ),
    )

    steering_axle_model = forms.ModelChoiceField(
        queryset=SteeringAxle.objects.all(),
        label="Модель управляемого моста: ",
        empty_label="Выберите модель",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    serial_number_of_the_steered_axle = forms.CharField(
        label="Заводской номер управляемого моста: ",
        widget=forms.TextInput(
            attrs={"placeholder": "Укажите номер", "class": "form-control auth-width"}
        ),
    )

    supply_contract = forms.CharField(
        label="Номер и дата договора поставки: ",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Укажите номер и дату",
                "class": "form-control auth-width",
            }
        ),
    )

    date_shipped_from_factory = forms.DateField(
        label="Дата отгрузки с завода: ",
        widget=forms.DateInput(
            attrs={"placeholder": "Укажите дату", "class": "form-control auth-width"}
        ),
    )

    consignee = forms.CharField(
        label="Грузополучатель (конечный потребитель): ",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Укажите грузополучателя",
                "class": "form-control auth-width",
            }
        ),
    )

    delivery_address = forms.CharField(
        label="Адрес поставки (эксплуатации): ",
        widget=forms.TextInput(
            attrs={"placeholder": "Укажите адрес", "class": "form-control auth-width"}
        ),
    )

    equipment = forms.CharField(
        label="Комплектация (дополнительные опции): ",
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Введите текст", "class": "form-control auth-width"}
        ),
    )

    client = forms.ModelChoiceField(
        queryset=User.objects.all().filter(user_role="CL"),
        label="Клиент: ",
        empty_label="Выберите клиента",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    service_company = forms.ModelChoiceField(
        queryset=ServiceCompany.objects.all(),
        label="Сервисная компания: ",
        empty_label="Выберите компанию",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )
