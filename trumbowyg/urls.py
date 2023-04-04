from django.urls import re_path

from trumbowyg.views import upload_image


urlpatterns = [
    re_path('^upload_image/$', upload_image, name='trumbowyg_upload_image'),
]
