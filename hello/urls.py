from django.urls import URLPattern

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("vinay", views.vinay, name="vinay")
]