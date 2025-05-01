from django.shortcuts import render
from .models import WebSection

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
