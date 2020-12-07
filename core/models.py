from django.db import models

# Create your models here.
class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()

    class Meta:
        ordering = ['created']

class Job(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    bigDescription = models.TextField()
    smallDescription = models.CharField(max_length=100, blank=True, default='')
    descFormation = models.TextField()
    video = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    SimilarJob = models.ManyToManyField("self")
    profile = models.ManyToManyField(Profile)

