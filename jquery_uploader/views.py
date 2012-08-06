# -*- coding: utf-8 -*-
import hashlib
import os
import time

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

from jquery_uploader.settings import *
from jquery_uploader.utils import *


def get(request):
    """
    Get preview for file. As usual in the relative path to the
    FileField MEDIA_ROOT, then initialize them only.
    """

    name = request.GET.get('name')
    print name
    full_name = os.path.join(settings.MEDIA_ROOT, name)
    print full_name
    thumb_url = get_thumb(full_name)
    file_name = os.path.basename(full_name)
    obj = get_object(file_name)
    full_url = os.path.join(settings.MEDIA_ROOT, name)
    print full_url

    result = []
    result.append({
        'delete_type': 'POST',
        'delete_url': reverse('jquery_upload_delete', args=[file_name, ]),
        'name': obj.original_name,
        'size': 0,
        'thumbnail_url': thumb_url,
        'url': full_url,
    })

    return HttpResponse(simplejson.dumps(result), mimetype='application/json')


def upload(request):
    if request.method == 'POST':
        uploaded = request.FILES.get('files[]', None)

        #generate hash for file name
        name, ext = os.path.splitext(uploaded.name)
        name_hash = hashlib.md5('%s%s' % (name, time.time())).hexdigest()
        file_name = '%s%s' % (name_hash, ext)
        real_file = os.path.join(uploader_root_rel, file_name)

        # write a file to a temporary directory downloads
        full_name = os.path.join(uploader_root, file_name)
        dest = open(full_name, 'wb+')
        for chunk in uploaded.chunks():
            dest.write(chunk)
        dest.close()

#        obj = save_object(user, uploaded.name, file_name)

        full_url = os.path.join(uploader_url, file_name)
        thumb_url = get_thumb(full_name)

        result = []
        result.append({
            'delete_type': 'POST',
            'delete_url': reverse('jquery_uploader_delete', args=[file_name, ]),
            'name': uploaded.name,
            'real_file': real_file,
            'size': uploaded.size,
            'thumbnail_url': thumb_url,
            'url': full_url,
        })

        return HttpResponse(simplejson.dumps(result), mimetype='application/json')


# TODO: function needs some work 
@csrf_exempt
def delete(request, file_name):
    file_name = os.path.basename(file_name)
    full_name = os.path.join(uploader_root, file_name)
    print full_name
    return HttpResponse('ok')
