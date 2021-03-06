from django.core.files.storage import default_storage
from django import template
from django.utils.encoding import force_str
import re

register = template.Library()


@register.filter(name="does_it_exist")
def does_it_exist(name):
    image = name.username + ".png"
    return default_storage.exists(image)


@register.filter("intspace")
def intspace(value):
    """
    Converts an integer to a string containing spaces every three digits.
    For example, 3000 becomes '3 000' and 45000 becomes '45 000'.
    See django.contrib.humanize app
    """
    orig = force_str(value)
    new = re.sub("^(-?\d+)(\d{3})", "\g<1> \g<2>", orig)
    if orig == new:
        return new
    else:
        return intspace(new)
