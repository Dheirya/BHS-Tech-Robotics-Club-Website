from django.shortcuts import render
from .models import Image, Team, Topic, Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'TechApp/index.html', {'projects': projects})


def topic(request, title):
    topic = Topic.objects.get(title=title)
    projects = Project.objects.filter(topic=topic)
    return render(request, 'TechApp/topic.html', {'topic': topic, 'projects': projects})
