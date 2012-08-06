import os
from PIL import Image

from .models import JqueryUploader
from .settings import *


def get_thumb(full_name):
    """ Generate and save thumbnail. Return thumbnail url """

    file_name = os.path.basename(full_name)
    name, ext = os.path.splitext(file_name)

    thumb_name = '%s_t%s' % (name, ext)
    thumb_full = os.path.join(uploader_root, thumb_name)
    if not os.path.exists(thumb_full):
        im = Image.open(full_name)
        thumb_image = im.copy()
        thumb_image.thumbnail(uploader_size, Image.ANTIALIAS)
        thumb_image.save(thumb_full, 'JPEG', quality=90)

    thumb_url = os.path.join(uploader_url, thumb_name)

    return thumb_url


def save_object(user, original_name, file_hash):
    obj = JqueryUploader(original_name=original_name, file_hash=file_hash)
    if user:
        obj.user = user
    obj.save()

    return obj


def get_object(file_hash):
    try:
        obj = JqueryUploader.objects.get(file_hash=file_hash)
    except JqueryUploader.DoesNotExist:
        obj = None
    return obj
