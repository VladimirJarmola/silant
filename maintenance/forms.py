from django import forms
from django.db.models import Q
from cars.models import Cars
from deskbook.models import ViewMaintenance

from maintenance.models import Maintenance
from users.models import ServiceCompany


class AddMaintenanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if "car_id" in kwargs:
            car_id = kwargs.pop("car_id")
            qs_car = Cars.objects.filter(id=car_id)
            # список ТО машины car_id
            maintenance_list = (
                Maintenance.objects.all()
                .filter(car__id=car_id)
                .values_list("view_maintenance", flat=True)
            )
            # queryset без проведенных ТО
            qs_view_maintenance = ViewMaintenance.objects.exclude(
                Q(pk__in=maintenance_list)
            )
        else:
            qs_car = Cars.objects.all()
            qs_view_maintenance = ViewMaintenance.objects.all()
        super(AddMaintenanceForm, self).__init__(*args, **kwargs)
        self.fields["car"].queryset = qs_car
        self.fields["view_maintenance"].queryset = qs_view_maintenance

    class Meta:
        model = Maintenance
        fields = "__all__"

    view_maintenance = forms.ModelChoiceField(
        queryset=None,
        label="Вид технического обслуживания: ",
        empty_label="Выберите ТО",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    Date_maintenance = forms.DateField(
        label="Дата проведения технического обслуживания: ",
        widget=forms.DateInput(
            attrs={"placeholder": "Укажите дату", "class": "form-control auth-width"}
        ),
    )

    operating_hours = forms.IntegerField(
        label="Наработка, моточас: ",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите число",
                "class": "form-control auth-width",
            }
        ),
    )

    work_order_number = forms.CharField(
        label="№ заказ-наряда: ",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите номер",
                "class": "form-control auth-width",
            }
        ),
    )

    work_order_date = forms.DateField(
        label="Дата выдачи заказ-наряда: ",
        widget=forms.DateInput(
            attrs={"placeholder": "Укажите дату", "class": "form-control auth-width"}
        ),
    )

    car = forms.ModelChoiceField(
        queryset=None,
        label="Машина: ",
        empty_label="Выберите машину",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    service_company = forms.ModelChoiceField(
        queryset=ServiceCompany.objects.all(),
        label="Сервисная компания: ",
        empty_label="Выберите компанию",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )
