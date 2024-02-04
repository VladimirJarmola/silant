from dataclasses import fields
from django import forms
from cars.models import Cars
from deskbook.models import FailureNode, RecoveryMethod

from reclamation.models import Reclamation
from users.models import ServiceCompany


class AddReclamationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if "car_id" in kwargs:
            car_id = kwargs.pop("car_id")
            qs_car = Cars.objects.filter(id=car_id)
            sc_id = Cars.objects.filter(id=car_id).values_list('service_company', flat=True)[0]
            qs_sc = ServiceCompany.objects.filter(id=sc_id)
        else:
            qs_car = Cars.objects.all()
            qs_sc = ServiceCompany.objects.all()
        super(AddReclamationForm, self).__init__(*args, **kwargs)
        self.fields["car"].queryset = qs_car
        self.fields["service_company"].queryset = qs_sc
        
    class Meta:
        model = Reclamation
        fields = '__all__'

    date_of_refusal = forms.DateField(
        label="Дата отказа: ",
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

    failure_node = forms.ModelChoiceField(
        queryset=FailureNode.objects.all(),
        label="Узел отказа: ",
        empty_label="Выберите узел",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    description_of_failure = forms.CharField(
        label="Описание отказа: ",
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Введите текст", "class": "form-control auth-width"}
        ),
    )

    recovery_method = forms.ModelChoiceField(
        queryset=RecoveryMethod.objects.all(),
        label="Способ восстановления: ",
        empty_label="Выберите способ",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )

    parts_used = forms.CharField(
        label="Используемые запасные части: ",
        required=False,
        widget=forms.Textarea(
            attrs={"placeholder": "Введите текст", "class": "form-control auth-width"}
        ),
    )

    restore_date = forms.DateField(
        label="Дата восстановления: ",
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
        queryset=None,
        label="Сервисная компания: ",
        empty_label="Выберите компанию",
        widget=forms.Select(attrs={"class": "form-select auth-width"}),
    )
    