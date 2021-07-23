from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 

# Create your models here.




class UserManager(BaseUserManager): 
    def _create_user(self, email, username, password, **extra_fields): 
        """ 
        Create and save a user with the given username, email, and password. 
        """ 
        if not email: 
            raise ValueError('The given email must be set') 
        email = self.normalize_email(email) 
        username = self.model.normalize_username(username) 
        user = self.model(email=email, username=username, **extra_fields) 
        user.set_password(password) 
        user.save(using=self._db) 
        return user 

 
    def create_user(self, email, username='', password=None, **extra_fields): 
        extra_fields.setdefault('is_staff', False) 
        extra_fields.setdefault('is_superuser', False) 
        return self._create_user(email, username, password, **extra_fields) 

    def create_superuser(self, username, email, password, **extra_fields): 
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True) 

 
        if extra_fields.get('is_staff') is not True: 
            raise ValueError('Superuser must have is_staff=True.') 
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError('Superuser must have is_superuser=True.') 
 
 
        return self._create_user(email, 'blogs/like_section.html',  password, **extra_fields) 


class User( AbstractUser ):
	
    
    user_image = models.ImageField(blank=True,upload_to="images")

    REQUIRED_FIELDS = [  'email', ]

    USERNAME_FIELD = 'username'

