from django import template
from django.apps import apps
from django.utils.http import urlencode


register = template.Library()

# @register.simple_tag()
# def tag_all_deskbook():
#     app_info = apps.get_app_config('deskbook')
    
#     list_name = []
#     for model in app_info.models:
#         list_name.append(app_info.models[model].__dict__['_meta'].verbose_name)
#     return list_name

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
