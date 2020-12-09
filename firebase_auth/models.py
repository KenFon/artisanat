from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                                    PermissionsMixin
                                                    
# Create your models here.
class UserCustomManager(BaseUserManager):
    """Custom UserManager Models that support firebase authentication"""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Vous devez avoir un mail valide")
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
            )
        user.save(using=self._db)
        return user

class UserCustom(AbstractBaseUser, PermissionsMixin):
    """Custom user model that support firebase authentication"""
    username = models.CharField(max_length=50, blank=True, default='')
    password = None
    email = models.EmailField(max_length=50, unique=True)
    location = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uid = models.CharField(max_length=100, default="")

    objects = UserCustomManager()
    USERNAME_FIELD = 'email'
    class Meta:
        ordering = ['created_at']