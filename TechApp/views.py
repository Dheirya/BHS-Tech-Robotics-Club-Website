from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Topic, Project, Tag
from ipware import get_client_ip
from .forms import CommentForm


def like(request):
    if request.method == "POST":
        project_id = request.POST.get("project_id")
        project = Project.objects.get(id=project_id)
        project.likes += 1
        project.save()
        return JsonResponse({"likes": project.likes})


def index(request):
    projects = Project.objects.all().order_by('?')
    return render(request, 'TechApp/index.html', {'projects': projects})


def search(request, query):
    projects = (Project.objects.filter(title__icontains=query) | Project.objects.filter(blurb__icontains=query) | Project.objects.filter(description__icontains=query)).distinct()
    return render(request, 'TechApp/search.html', {'projects': projects, 'query': query})


def topic(request, title):
    topic = Topic.objects.get(title=title)
    projects = Project.objects.filter(topic=topic)
    return render(request, 'TechApp/topic.html', {'topic': topic, 'projects': projects})


def tag(request, name):
    tag = Tag.objects.get(name=name)
    projects = Project.objects.filter(tags=tag)
    return render(request, 'TechApp/tag.html', {'tag': tag, 'projects': projects})


def project(request, title):
    project = Project.objects.get(title=title)
    images = project.images.all()
    project_updates = project.projectupdate_set.all().order_by('-date')
    form = CommentForm(request.POST or None)
    comments = project.comment_set.all().order_by('-created_at')
    ip = str(get_client_ip(request)[0])
    if form.is_valid():
        comment = form.save(commit=False)
        comment.project = project
        comment.ip_address = ip
        if project.comment_set.filter(ip_address=ip).count() >= 3:
            form.add_error(None, "You have already commented 3 times on this project! Comment on another project.")
            return render(request, 'TechApp/project.html', {'project': project, 'images': images, 'updates': project_updates, 'form': form, 'comments': comments})
        comment.save()
        return redirect('project', title=title)
    return render(request, 'TechApp/project.html', {'project': project, 'images': images, 'updates': project_updates, 'form': form, 'comments': comments})

