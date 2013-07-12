from django import template
from django.conf import settings

from jquery_uploader import settings as uploader_settings

register = template.Library()


@register.inclusion_tag('jquery_uploader/simple.html')
def jquery_uploader_simple(max_file_size=None):
    if max_file_size is None:
        max_file_size = uploader_settings.uploader_max_file_size
    return {
        'max_file_size': max_file_size,
        'preview_max_height': uploader_settings.uploader_preview_max_height,
        'preview_max_width': uploader_settings.uploader_preview_max_width,
    }


@register.inclusion_tag('jquery_uploader/bootstrap.html')
def jquery_uploader_bootstrap(max_file_size=None):
    if max_file_size is None:
        max_file_size = uploader_settings.uploader_max_file_size
    return {
        'max_file_size': max_file_size,
        'preview_max_height': uploader_settings.uploader_preview_max_height,
        'preview_max_width': uploader_settings.uploader_preview_max_width,
    }


@register.inclusion_tag('jquery_uploader/jquery-ui.html')
def jquery_uploader_jqueryui(max_file_size=None):
    if max_file_size is None:
        max_file_size = uploader_settings.uploader_max_file_size
    return {
        'max_file_size': max_file_size,
        'preview_max_height': uploader_settings.uploader_preview_max_height,
        'preview_max_width': uploader_settings.uploader_preview_max_width,
    }
