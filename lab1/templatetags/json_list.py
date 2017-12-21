import json

from django import template

register = template.Library()


@register.inclusion_tag('tags/json_list.html')
def json_list(obj):
    obj = [None if item is None else float(item) for item in obj]
    data = json.dumps(obj)
    return {'data': data}
