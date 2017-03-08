# coding=utf-8
from django.conf import settings
from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
from django.utils.translation import get_language, get_language_info
from django.core.urlresolvers import reverse


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
        ] + ['trumbowyg/langs/%s.min.js' % x[0] for x in settings.LANGUAGES]

    def render(self, name, value, attrs=None):
        output = super(TrumbowygWidget, self).render(name, value, attrs)
        script = u'''
            <script>
                $("#id_%s").trumbowyg({
                    lang: "%s",
                    semantic: true,
                    resetCss: true,
                    autogrow: true,
                    removeformatPasted: true,
                    btnsDef: {
                        image: {
                            dropdown: ['upload', 'insertImage', 'base64', 'noembed'],
                            ico: 'insertImage'
                        }
                    },
                    btns: [
                        ['formatting'],
                        'btnGrp-semantic',
                        ['link'],
                        ['image'],
                        'btnGrp-justify',
                        'btnGrp-lists',
                        'video',
                        ['horizontalRule'],
                        ['removeformat'],
                        ['fullscreen'],
                        ['viewHTML']
                    ],
                    plugins: {
                        upload: {
                            serverPath: '%s',
                            fileFieldName: 'image',
                            statusPropertyName: 'message',
                            urlPropertyName: 'file'
                        }
                    }
                });
            </script>
        ''' % (name, get_language_info(get_language())['code'], reverse('trumbowyg_upload_image'))
        output += mark_safe(script)
        return output
