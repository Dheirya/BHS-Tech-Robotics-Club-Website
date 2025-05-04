from django.db import models

# Create your models here.

class WebSection(models.Model):
    title = models.CharField(max_length = 100)
    def __str__(self):
        return self.title
    blurb = models.CharField(max_length = 500)
    description = models.CharField()
    choice_tuple = [
        ('hardware', 'Hardware Project'),
        ('software', 'Software Project'),
        ('event', 'Event'),
        ('member', 'Personal Project')
    ]
    section = models.CharField(max_length = 100, choices = choice_tuple)