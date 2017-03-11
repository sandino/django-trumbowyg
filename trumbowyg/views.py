# coding=utf-8

import os
import json

from PIL import Image
from django.conf import settings
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from trumbowyg import settings as _settings
from trumbowyg.forms import ImageForm


@csrf_exempt
@require_POST
def upload_image(request):
    if not request.is_ajax():
        return HttpResponse(status=400)    # bad request
    if not (request.user.is_active and request.user.is_staff):
        return HttpResponse(status=403)    # forbidden

    image_form = ImageForm(request.POST, request.FILES)
    if image_form.is_valid():
        image = image_form.cleaned_data['image']
        url = save_image(image)
        context = {'message': 'uploadSuccess', 'file': url}
    else:
        context = {'message': image_form.errors['image'][0]}

    return HttpResponse(json.dumps(context), content_type='application/json')


def save_image(image):
    """Receives image, saves it and returns its url"""
    path = os.path.join(_settings.UPLOAD_PATH, image.name)
    if _settings.THUMBNAIL_SIZE:
        im = Image.open(image)
        initial_size = im.size
        im.thumbnail(_settings.THUMBNAIL_SIZE)
        if im.size != initial_size:  # if original is larger than thumbnail
            real_path = os.path.join(_settings.UPLOAD_PATH,
                                     'thumb_%s' % image.name)
            try:
                im.save(os.path.join(settings.MEDIA_ROOT, real_path), "JPEG")
                return real_path
            except IOError:
                print ("cannot create thumbnail for", image)
                return

    real_path = default_storage.save(path, image)

    return default_storage.url(real_path)

