from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("topic/<str:title>/", views.topic, name="topic"),
    path("project/<str:title>/", views.project, name="project")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
