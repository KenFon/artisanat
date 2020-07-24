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
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
