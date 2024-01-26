from django.utils.http import urlencode
from django import template

from cars.models import ServiceCompany

from deskbook.models import FailureNode, RecoveryMethod


register = template.Library()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)


@register.simple_tag()
def tag_failure_node():
    return FailureNode.objects.all()


@register.simple_tag()
def tag_recovery_method():
    return RecoveryMethod.objects.all()

@register.simple_tag()
def tag_service_company():
    return ServiceCompany.objects.all().exclude(name="самостоятельно")
