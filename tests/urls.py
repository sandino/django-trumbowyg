from django.urls import path, include

urlpatterns = [
    path(r"", include("trumbowyg.urls")),
]
