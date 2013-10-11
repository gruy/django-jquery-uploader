# -*- coding: utf-8 -*-
import magic
import os
from PIL import Image

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from jquery_uploader.settings import *


def thumb_name(full_name):
    """ Generate thumb file name """
    file_name = os.path.basename(full_name)
    name, ext = os.path.splitext(file_name)
    thumb = '%s_t.jpeg' % name
    return thumb


def get_thumb(full_name):
    """ Generate and save thumbnail. Return thumbnail url """

    thumb_url = None
    thumb = thumb_name(full_name)
    thumb_full = os.path.join(uploader_root, thumb)

    mimes_images = ('image/png', 'image/jpeg', 'image/pjpeg', 'image/gif', 'image/x-ms-bmp', 'image/bmp', 'image/vnd.microsoft.icon')
    mime = magic.from_file(full_name, mime=True)
    if mime in mimes_images:
        if not os.path.exists(thumb_full):
            im = Image.open(full_name)
            thumb_image = im.copy()
            if thumb_image.mode != 'RGB':
                thumb_image = thumb_image.convert('RGB')
            thumb_image.thumbnail(uploader_size, Image.ANTIALIAS)
            thumb_image.save(thumb_full, 'JPEG', quality=80)

        thumb_url = os.path.join(uploader_url, thumb)

    return thumb_url


def save_to_model(file_field, file_name):
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(open(os.path.join(settings.MEDIA_ROOT, file_name), 'r').read())
    img_temp.flush()
    file_field.save(os.path.basename(file_name), File(img_temp), save=False)
    # delete files after saving in models
    delete_file(file_name)


def delete_file(file_name):
    file_name = os.path.basename(file_name)
    full_name = os.path.join(uploader_root, file_name)
    thumb = thumb_name(full_name)
    thumb_full = os.path.join(uploader_root, thumb)

    try:
        os.unlink(full_name)
    except OSError:
        pass

    try:
        os.unlink(thumb_full)
    except OSError:
        pass
