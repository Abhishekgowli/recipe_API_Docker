from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager): 

    def create_user(self, email, password=None, **extra_fields):
        """create user """
        if not email: 
            raise ValueError("user must have a email adddress")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_supperuser(self, email, password):
        """creates a super user """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_supperuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
