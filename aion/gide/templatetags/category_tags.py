#coding=utf-8
from django.template.base import Library
from aion.gide.models import Pages

register = Library()

@register.inclusion_tag("templatetags/category_menu.html", takes_context=True)
def category_menu(context):
    root_nodes = Pages.objects.root_nodes().filter(status=2)
    return {
        'menu': root_nodes
    }
