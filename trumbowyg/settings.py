# coding=utf-8

from django.conf import settings

UPLOAD_PATH = getattr(settings, 'TRUMBOWYG_UPLOAD_PATH', 'uploads/')
THUMBNAIL_SIZE = getattr(settings, 'TRUMBOWYG_THUMBNAIL_SIZE', None)
TRANSLITERATE_FILENAME = getattr(settings, 'TRUMBOWYG_TRANSLITERATE_FILENAME', False)
SEMANTIC = getattr(settings, 'TRUMBOWYG_SEMANTIC', 'false')
