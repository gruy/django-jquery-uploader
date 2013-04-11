# -*- coding: utf-8 -*-
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
    thumb = '%s_t%s' % (name, ext)
    return thumb


def get_thumb(full_name):
    """ Generate and save thumbnail. Return thumbnail url """

    thumb = thumb_name(full_name)
    thumb_full = os.path.join(uploader_root, thumb)

    if not os.path.exists(thumb_full):
        im = Image.open(full_name)
        thumb_image = im.copy()
        thumb_image.thumbnail(uploader_size, Image.ANTIALIAS)
        thumb_image.save(thumb_full, 'JPEG', quality=90)

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
