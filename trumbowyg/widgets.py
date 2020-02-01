# coding=utf-8
from django.conf import settings as django_settings
from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
from django.utils.translation import get_language

from . import settings

try:
    from django.urls import reverse
except ImportError:
    # For old versions of django
    from django.core.urlresolvers import reverse


def get_trumbowyg_language():
    """
    Get and convert language from django to trumbowyg format

    Example:
        Django uses: pt-br and trumbowyg use pt_br
    """
    language = getattr(settings, 'TRUMBOWYG_LANGUAGE', django_settings.LANGUAGE_CODE)
    return language.replace('-', '_')


class TrumbowygWidget(Textarea):
    class Media:
        css = {
            'all': (
                'trumbowyg/ui/trumbowyg.css',
                'trumbowyg/admin.css',
            )
        }
        js = [
            '//ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
            'trumbowyg/trumbowyg.min.js',
            'trumbowyg/plugins/upload/trumbowyg.upload.js',
            'trumbowyg/langs/{0}.min.js'.format(get_trumbowyg_language())
        ]

    def render(self, name, value, attrs=None, renderer=None):
        output = super(TrumbowygWidget, self).render(name, value, attrs)
        script = u'''
            <script>
                $("#id_{name}").trumbowyg({{
                    lang: "{lang}",
                    semantic: {semantic},
                    resetCss: true,
                    autogrow: true,
                    removeformatPasted: true,
                    btnsDef: {{
                        image: {{
                            dropdown: ["upload", "insertImage", "base64", "noembed"],
                            ico: "insertImage"
                        }}
                    }},
                    btns: [
                        ["formatting"],
                        "btnGrp-semantic",
                        ["link"],
                        ["image"],
                        "btnGrp-justify",
                        "btnGrp-lists",
                        ["horizontalRule"],
                        ["removeformat"],
                        ["viewHTML"],
                        ["fullscreen"]
                    ],
                    plugins: {{
                        upload: {{
                            serverPath: "{path}",
                            fileFieldName: "image",
                            statusPropertyName: "message",
                            urlPropertyName: "file"
                        }}
                    }}
                }});
            </script>
        '''.format(
            name=name,
            lang=get_trumbowyg_language(),
            semantic=settings.SEMANTIC,
            path=reverse('trumbowyg_upload_image'),
        )
        output += mark_safe(script)
        return output
