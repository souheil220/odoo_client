from django.core.files.storage import default_storage
from django import template

register = template.Library()


@register.filter(name="does_it_exist")
def does_it_exist(name):
    image = name.username + ".png"
    return default_storage.exists(image)
