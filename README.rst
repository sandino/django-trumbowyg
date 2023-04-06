Introduction
============

django-trumbowyg is the Django-related reusable app for integrating `Trumbowyg WYSIWYG editor <http://alex-d.github.io/Trumbowyg/>`_. It is recognized as one of the `best WYSIWYG editors <https://github.com/iDoRecall/comparisons/blob/master/JavaScript-WYSIWYG-editors.md>`_.


Installation
============

1. Install ``django-trumbowyg`` using ``pip``::

    $ pip install django-trumbowyg

2. Add ``'trumbowyg'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'trumbowyg',
        ...
    )

3. Update your ``urls.py``::

    url(r'^trumbowyg/', include('trumbowyg.urls'))

4. Sometimes you might want to limit size of uploaded images, e.g. if they are too large. In this case just put in settings (if you omit this, the image will be uploaded unchanged)::

    TRUMBOWYG_THUMBNAIL_SIZE = (1920, 1080)

5. The package will try to use the language defined in ``LANGUAGE_CODE`` and if this language isin't availabe the default is ``en`` 

6. (Optional) If you wish image filenames to be transliterated, install `unidecode <https://pypi.org/project/Unidecode/>`_ from PyPi and set::

    TRUMBOWYG_TRANSLITERATE_FILENAME = True

7. Set [semantics](https://alex-d.github.io/Trumbowyg/documentation/#semantic) if necessary. It defaults to ``false``::

    TRUMBOWYG_SEMANTIC = 'true'

8. Don't forget to add ``{{ form.media }}`` to form template.

Usage
=====

Use ``TrumbowygWidget`` in your forms::

    from django.forms import ModelForm
    from django.contrib.admin import ModelAdmin
    from trumbowyg.widgets import TrumbowygWidget
    from your_app.models import YourModel

    class YourModelAdminForm(ModelForm):
        class Meta:
            model = YourModel
            widgets = {
                'text': TrumbowygWidget(),
            }

    class YourModelAdmin(admin.ModelAdmin):
        form = YourModelAdminForm


    admin.site.register(YourModel, YourModelAdmin)


Credits
=======

- `Alex-D <http://alex-d.fr/>`_
