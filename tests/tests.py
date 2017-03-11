import json
import os

from PIL import Image
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.test.client import Client
from django.test.utils import setup_test_environment
from django.urls import reverse
from django.utils.six import BytesIO

from trumbowyg.forms import ImageForm


def create_image(filename, storage=None, size=(400, 200), image_mode='RGB',
                 image_format='JPEG'):
    """
    Generate a test image, returning the filename that it was saved as.

    If ``storage`` is ``None``, the BytesIO containing the image data
    will be passed instead.
    """
    data = BytesIO()
    Image.new(image_mode, size).save(data, image_format)
    data.seek(0)
    if not storage:
        return data
    image_file = ContentFile(data.read())
    return storage.save(filename, image_file)


class UploadTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            'tmp', 'tmp@example.com', 'tmp', **{'is_staff': True})
        self.client = Client()
        setup_test_environment()    # This creates request context
        image_data = create_image('uploads/image.jpg')
        self.image_to_upload = SimpleUploadedFile(
            'image.jpg', image_data.getvalue())

    def test_upload_post(self):
        self.client.login(username='tmp', password='tmp')
        response = self.client.post(
            reverse('trumbowyg_upload_image'),
            {'image': self.image_to_upload},
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            'message': 'uploadSuccess',
            'file': 'uploads/thumb_image.jpg'
        })
        # unlink test file
        image_path = 'media/' + json.loads(response.content)['file']
        if os.path.isfile(image_path):
            os.unlink(image_path)

    def test_form(self):
        form_data = {'image': self.image_to_upload}
        form = ImageForm(files=form_data)
        self.assertTrue(form.is_valid())
