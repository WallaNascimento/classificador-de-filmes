from django.db import models

#from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager

class User_manager(BaseUserManager):
    def create_user(self, username, email, number, password):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, number=number)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, number, password):
        user = self.create_user(username=username, email=email, number=number, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True, )
    email = models.EmailField(max_length=32, unique=True)
    #gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Others")]
    #number = models.CharField(choices=gender_choices, default="M", max_length=1)
    number = models.CharField(max_length=32, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ['username', 'number']
    USERNAME_FIELD = "email"
    objects = User_manager()

    def has_perm(self, perm, obj=None):
        return True #self.is_admin

    def has_module_perms(self, app_label):
        return True# self.is_admin
    
    def __str__(self):
        return self.username

