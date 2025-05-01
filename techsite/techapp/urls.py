from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("STEM/", views.stem, name="STEM"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("<str:ids>/", views.general, name="Section"),
    path("<str:section>/<str:id>/", views.pinpoint, name="Project")
]