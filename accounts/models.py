from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from accounts.managers import User_manager
# Create your models here.


GENDER = (
    ("Male",'Male'),
    ("Female",'Female'),
    ("Other",'Other'),
)

class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25,unique=True)
    profile_pic = models.ImageField(upload_to='profiles',default='profiles/profile.png')
    phone = models.CharField(max_length=10,unique=True)
    gender = models.CharField(choices=GENDER,max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name','phone','gender']
    objects = User_manager()