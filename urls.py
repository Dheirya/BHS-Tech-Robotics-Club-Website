"""
URL configuration for TechClubSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from TechApp.models import Project, Topic, Tag

projects_dict = {
    'queryset': Project.objects.all()
}
tags_dict = {
    'queryset': Tag.objects.all()
}
topics_dict = {
    'queryset': Topic.objects.all()
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("TechApp.urls")),
    path('tinymce/', include('tinymce.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": {"projects": GenericSitemap(projects_dict, priority=1.0, changefreq='weekly'), "topics": GenericSitemap(topics_dict, priority=0.7, changefreq='monthly'), "tags": GenericSitemap(tags_dict, priority=0.4, changefreq='monthly')}}, name='django.contrib.sitemaps.views.sitemap'),
]
