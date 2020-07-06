from django import template

from office.models import Department
register = template.Library()


@register.simple_tag()
def get_dep():
    return Department.objects.all()
