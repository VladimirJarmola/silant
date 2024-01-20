from django.utils.http import urlencode
from django import template

from deskbook.models import DriveAxle, EngineModel, SteeringAxle, TransmissionModel, VehicleModel


register = template.Library()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)


@register.simple_tag()
def tag_vehicle_models():
    return VehicleModel.objects.all()


@register.simple_tag()
def tag_engine_models():
    return EngineModel.objects.all()


@register.simple_tag()
def tag_transmission_models():
    return TransmissionModel.objects.all()


@register.simple_tag()
def tag_drive_axle_models():
    return DriveAxle.objects.all()


@register.simple_tag()
def tag_steering_axle_models():
    return SteeringAxle.objects.all()
