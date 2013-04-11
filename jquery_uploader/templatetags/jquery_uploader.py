from django import template
from django.conf import settings


register = template.Library()


# @register.inclusion_tag('jquery_uploader/jquery_uploader_bootstrap.html')
@register.inclusion_tag('jquery_uploader/bootstrap.html')
def jquery_uploader(max_file_size=2097152):
    return {
        'max_file_size': max_file_size,
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': settings.STATIC_URL,
    }
