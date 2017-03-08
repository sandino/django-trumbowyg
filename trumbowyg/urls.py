from django.conf.urls import url

from trumbowyg.views import upload_image


urlpatterns = [
    url('^upload_image/$', upload_image, name='trumbowyg_upload_image'),
]
