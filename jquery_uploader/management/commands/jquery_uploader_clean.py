# -*- coding: utf-8 -*-
import datetime, os

from django.core.management.base import NoArgsCommand

from jquery_uploader.settings import *


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        days_diff = datetime.datetime.today() - datetime.timedelta(days=uploader_days_diff)
        files = os.listdir(uploader_root)
        for name in files:
            full_name = os.path.join(uploader_root, name)
            file_date = datetime.datetime.fromtimestamp(os.stat(full_name).st_mtime)
            if file_date < days_diff:
                print 'Delete %s' % full_name
                os.unlink(full_name)
