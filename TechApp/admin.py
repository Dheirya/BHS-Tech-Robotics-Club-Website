from django.contrib import admin
from .models import Image, Topic, Project, ProjectUpdate, Comment, Tag


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "hidden")


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "coverImage")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "blurb", "link")


@admin.register(ProjectUpdate)
class ProjectUpdateAdmin(admin.ModelAdmin):
    list_display = ("project", "updateDescription", "date")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("project", "name", "content", "created_at", "ip_address")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "blurb")
