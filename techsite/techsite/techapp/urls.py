from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("STEM/", views.stem, name="STEM"),
    path("accounts/", include("django.contrib.auth.urls")),
path("STEM/judge/", views.judge_page, name="Judge Page"),
    path("STEM/team/", views.team_page, name="Team Page"),
    path("<str:ids>/", views.general, name="Section"),
    path("<str:section>/<str:id>/", views.pinpoint, name="Project"),
]