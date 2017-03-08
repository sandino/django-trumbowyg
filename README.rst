Introduction
============

django-trumbowyg is the Django-related reusable app for integrating `Trumbowyg WYSIWYG editor <http://alex-d.github.io/Trumbowyg/>`_.

Initially this package was forked from `Django FS Trumbowyg <https://bitbucket.org/fogstream/django-fs-trumbowyg/>`_ package and then reworked.


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

4. Sometimes you might want to limit size of uploaded images, e.g. if it is too large. In this case just put in settings::

    TRUMBOWYG_THUMBNAIL_SIZE = (1920, 1080)
	
If you omit this, the image will be uploaded unchanged.


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

- `Fogstream <http://fogstream.ru/>`_
- `Alex-D <http://alex-d.fr/>`_
