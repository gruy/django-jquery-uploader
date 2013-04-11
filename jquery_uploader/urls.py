from django.conf.urls import patterns, include, url


urlpatterns = patterns('jquery_uploader.views',
    url(r'^delete/(?P<file_name>.*)/$', 'delete', name='jquery_uploader_delete'),
    url(r'^upload/$', 'upload', name='jquery_uploader'),
)
