from django.utils.http import urlencode
from django import template

from deskbook.models import FailureNode, RecoveryMethod, ServiceCompany


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
    return ServiceCompany.objects.all()

@register.simple_tag()
def tag_list_deskbook():
    list_deskbook = ['failure_node', 'recovery_method']
    return list_deskbook
