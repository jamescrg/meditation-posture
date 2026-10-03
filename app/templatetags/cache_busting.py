import os

from django import template
from django.contrib.staticfiles import finders
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def static_versioned(path):
    """Return the URL of a static file with its modification time appended,
    so that browsers fetch a fresh copy whenever the file changes."""

    url = static(path)
    file_path = finders.find(path)

    if file_path:
        url += "?v=" + str(int(os.path.getmtime(file_path)))

    return url
