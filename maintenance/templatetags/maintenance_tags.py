from django import template
from django.utils.http import urlencode

from cars.models import Cars, ServiceCompany

from deskbook.models import VehicleModel, ViewMaintenance


register = template.Library()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)


@register.simple_tag()
def tag_view_maintenance():
    return ViewMaintenance.objects.all()


@register.simple_tag()
def tag_serial_number_vehicle():
    return Cars.objects.all()


@register.simple_tag()
def tag_service_company():
    return ServiceCompany.objects.all()


@register.simple_tag()
def tag_list_deskbook():
    list_deskbook = ['view_maintenance']
    return list_deskbook
