from django.shortcuts import render, redirect
from .models import WebSection

def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

# Create your views here.
def home(request):
    return render(request, "home.html")

def general(request, ids):
    items = WebSection.objects.filter(section = ids)
    if ids == 'hardware':
        ids = 'Hardware Projects'
    else:
        if ids == 'software':
            ids = 'Software Projects'
        else:
            if ids == 'events':
                ids = 'Events'
            else:
                if ids == 'member':
                    ids = 'Member Projects'
                else:
                    ids = ''
    return render(request, "general.html", {"projects": items, "section": ids})

def pinpoint(request, section, id):
    item = WebSection.objects.get(title = id)
    return render(request, 'specific.html', {'item': item})

def stem(request):
    return render(request, 'stem.html')

def judge_page(request):
    user = request.user
    if has_group(user, 'Judge') | has_group(user, 'Developer') | has_group(user, 'Leadership'):
        return render(request, 'judge.html')
    else:
        return redirect(stem)

def team_page(request):
    user = request.user
    if has_group(user, 'Team') | has_group(user, 'Developer') | has_group(user, 'Leadership'):
        return render(request, 'team.html')
    else:
        return redirect(stem)