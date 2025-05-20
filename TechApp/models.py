from tinymce.models import HTMLField
from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/', help_text="Upload an image")
    title = models.CharField(max_length=250, unique=True, help_text="Title of the image")

    def __str__(self):
        return self.title

    @property
    def get_first_project_url(self):
        if self.project_set.exists():
            return '/project/' + self.project_set.first().title
        if self.topic_set.exists():
            return '/topic/' + self.topic_set.first().title
        return self.image.url


class Topic(models.Model):
    title = models.CharField(max_length=250, unique=True, help_text="Title of the topic")
    description = models.TextField(help_text="Description of the topic")
    coverImage = models.ForeignKey(Image, on_delete=models.CASCADE, help_text="Cover image for the topic")

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=250, unique=True, help_text="Title of the project")
    blurb = models.TextField(max_length=750, help_text="Short description of the project")
    description = HTMLField(help_text="Detailed description of the project")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, help_text="Topic related to the project")
    images = models.ManyToManyField(Image, help_text="Images related to the project")
    link = models.URLField(blank=True, null=True, help_text="External link to the project")
    likes = models.IntegerField(default=0, help_text="Number of likes for this project")
    tags = models.ManyToManyField('Tag', blank=True, help_text="Tags related to the project")

    def __str__(self):
        return self.title

    @property
    def random_image(self):
        return self.images.order_by('?').first()


class ProjectUpdate(models.Model):
    updateDescription = models.TextField(help_text="Description of the update")
    date = models.DateTimeField(auto_now_add=True, help_text="Date of the update")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text="Project related to the update")

    def __str__(self):
        return f"Update for {self.project.title} Project on {self.date.strftime('%m/%d/%Y')}"


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text="Project related to the comment")
    name = models.CharField(max_length=32, help_text="Name of the commenter")
    content = models.TextField(max_length=300, help_text="Content of the comment")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of the comment")
    ip_address = models.GenericIPAddressField(blank=True, null=True, help_text="IP address of the commenter")

    def __str__(self):
        return f"Comment by {self.name} on {self.created_at.strftime('%m/%d/%Y')}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="Name of the tag")
    blurb = models.TextField(max_length=750, help_text="Short description of the tag")

    def __str__(self):
        return self.name

