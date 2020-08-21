from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Vous devez avoir un email valide')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and saves a new super user"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'