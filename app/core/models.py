from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



class UserManager(BaseUserManager): 

    def create_user(self, email, password=None, **extra_fields):
        if not email: 
            raise ValueError("user must have a email adddress")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_supperuser(self, email, password):
        """creates a super user """
        user= self.create_user(email,password)
        user.is_staff=True
        user.is_supperuser=True
        user.save()

        return user




class User(AbstractBaseUser, PermissionsMixin):
    """customising the User Model That Supports email"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
