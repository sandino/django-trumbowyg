import logging

from django.utils.text import slugify as django_slugify

from trumbowyg import settings as _settings

logger = logging.getLogger(__name__)


def slugify(value):
    if _settings.TRANSLITERATE_FILENAME:
        try:
            from unidecode import unidecode

            value = unidecode(value)
        except ImportError as e:
            logger.exception(e)

    return django_slugify(value)
