import os

from django.conf import settings


uploader_days_diff = getattr(settings, 'JQUERY_UPLOADER_DAYS_DIFF', 1)

uploader_root_rel = getattr(settings, 'JQUERY_UPLOADER_ROOT', 'jquery_uploader')
uploader_root = os.path.join(settings.MEDIA_ROOT, uploader_root_rel)

uploader_url = os.path.join(settings.MEDIA_URL, getattr(settings, 'JQUERY_UPLOADER_URL', 'jquery_uploader'))

if not os.path.exists(uploader_root):
    os.makedirs(uploader_root)

uploader_preview_max_height = getattr(settings, 'JQUERY_UPLOADER_PREVIEW_MAX_HEIGHT', 140)
uploader_preview_max_width = getattr(settings, 'JQUERY_UPLOADER_PREVIEW_MAX_WIDTH', 200)

uploader_size = (uploader_preview_max_width, uploader_preview_max_height)

uploader_max_file_size = getattr(settings, 'JQUERY_UPLOADER_MAX_FILE_SIZE', 10485760)
