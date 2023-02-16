from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("some-page", views.some_page, name="some-page")
]
