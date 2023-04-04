from tempfile import NamedTemporaryFile

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from PIL import Image


def create_image():
    """
    Generate a test image.
    """
    tmp_file = NamedTemporaryFile(suffix=".jpg", delete=True)

    tmp_img = Image.new("RGB", size=(100, 100), color=(255, 0, 0))
    tmp_img.save(tmp_file, format="JPEG")

    tmp_file.seek(0)

    return tmp_file


class UploadTest(TestCase):
    def test_upload_post(self):
        User.objects.create_user("tmp", "tmp@example.com", "tmp", **{"is_staff": True})

        self.client.login(username="tmp", password="tmp")

        tmp_image = create_image()
        tmp_image_name = tmp_image.name.split("/")[-1]

        response = self.client.post(
            reverse("trumbowyg_upload_image"),
            {"image": tmp_image},
            **{"HTTP_X_REQUESTED_WITH": "XMLHttpRequest"},
        )

        expected = {"message": "uploadSuccess", "file": f"/uploads/{tmp_image_name}"}

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), expected)
