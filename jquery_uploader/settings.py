import os

from django.conf import settings

uploader_days_diff = getattr(settings, 'JQUERY_UPLOADER_DAYS_DIFF', 1)

uploader_root_rel = getattr(settings, 'JQUERY_UPLOADER_ROOT', 'jquery_uploader')
uploader_root = os.path.join(settings.MEDIA_ROOT, uploader_root_rel)

uploader_url = os.path.join(settings.MEDIA_URL, getattr(settings, 'JQUERY_UPLOADER_URL', 'jquery_uploader'))

if not os.path.exists(uploader_root):
    os.makedirs(uploader_root)

uploader_size = getattr(settings, 'JQUERY_UPLOADER_THUMB_SIZE', (80, 80))
