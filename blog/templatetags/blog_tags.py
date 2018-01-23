from django import template
from blog.models import Category
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def category_list():
    cat = Category.objects.all()
    html = render_to_string('blog/_category_list.html', {'cat': cat})
    return mark_safe(html)
