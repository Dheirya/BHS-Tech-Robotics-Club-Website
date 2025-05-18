from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    @property
    def get_first_project_url(self):
        if self.project_set.exists():
            return '/project/' + self.project_set.first().title
        if self.topic_set.exists():
            return '/topic/' + self.topic_set.first().title
        return self.image.url


class Team(models.Model):
    name = models.CharField(max_length=250, unique=True)
    teamMember = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    judges = models.ManyToManyField('auth.User', related_name='judges')

    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    coverImage = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    images = models.ManyToManyField(Image, blank=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def random_image(self):
        return self.images.order_by('?').first()


class ProjectUpdate(models.Model):
    updateDescription = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Update for {self.project.title} Project on {self.date.strftime('%m/%d/%Y')}"


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=32)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.created_at.strftime('%m/%d/%Y')}"
