from django import forms


class ImageForm(forms.Form):
    image = forms.ImageField()
