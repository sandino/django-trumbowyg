# coding=utf-8

from django.conf import settings


UPLOAD_PATH = getattr(settings, 'TRUMBOWYG_UPLOAD_PATH', 'uploads/')
THUMBNAIL_SIZE = getattr(settings, 'TRUMBOWYG_THUMBNAIL_SIZE', None)
