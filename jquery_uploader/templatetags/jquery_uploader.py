from django import template
from django.conf import settings


register = template.Library()


@register.inclusion_tag('jquery_uploader/jquery_uploader.html')
def jquery_uploader(files=None):
    return {
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': settings.STATIC_URL,
    }
