from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=250)
    teamMember = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    judges = models.ManyToManyField('auth.User', related_name='judges')

    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=250)
    blurb = models.TextField()
    description = models.TextField()
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=250)
    blurb = models.TextField()
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    authors = models.ManyToManyField('auth.User')
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.title

    @property
    def random_image(self):
        return self.images.order_by('?').first()
