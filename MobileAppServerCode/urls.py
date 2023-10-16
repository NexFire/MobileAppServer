from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("postInfo",views.postVratkaInfo),
    path("postPdf",views.postPdf)
]