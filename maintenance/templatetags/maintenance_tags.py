from django import template
from django.utils.http import urlencode

from cars.models import ServiceCompany

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
def tag_vehicle_models():
    return VehicleModel.objects.all()


@register.simple_tag()
def tag_service_company():
    return ServiceCompany.objects.all()
