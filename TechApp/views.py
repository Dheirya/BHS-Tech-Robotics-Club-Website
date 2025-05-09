from django.shortcuts import render
from .models import Image, Team, Topic, Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'TechApp/index.html', {'projects': projects})
