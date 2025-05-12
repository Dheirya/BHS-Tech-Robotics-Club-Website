from .models import Topic, Image


def all_topics(request):
    return {'all_topics': Topic.objects.all()}


def all_images(request):
    return {'all_images': Image.objects.all().order_by('?')}
