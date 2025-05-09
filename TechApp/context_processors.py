from .models import Topic


def all_topics(request):
    return {'all_topics': Topic.objects.all()}
