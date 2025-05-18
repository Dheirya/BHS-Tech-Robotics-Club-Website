from django.contrib import admin
from .models import Image, Team, Topic, Project, ProjectUpdate, Comment


admin.site.register(Image)
admin.site.register(Team)
admin.site.register(Topic)
admin.site.register(Project)
admin.site.register(ProjectUpdate)
admin.site.register(Comment)
