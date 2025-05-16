from django.shortcuts import render
from .models import Image, Team, Topic, Project


def index(request):
    projects = Project.objects.all().order_by('?')
    return render(request, 'TechApp/index.html', {'projects': projects})


def topic(request, title):
    topic = Topic.objects.get(title=title)
    projects = Project.objects.filter(topic=topic)
    return render(request, 'TechApp/topic.html', {'topic': topic, 'projects': projects})


def project(request, title):
    project = Project.objects.get(title=title)
    images = project.images.all()
    return render(request, 'TechApp/project.html', {'project': project, 'images': images})
