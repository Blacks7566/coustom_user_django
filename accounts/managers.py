from django.contrib.auth.models import BaseUserManager


class User_manager(BaseUserManager):

    def create_user(self,email,password,phone,name,gender,**extra_fields):
        if not email:
            raise ValueError("email needed for every user")
        
        email = self.normalize_email(email)

        user = self.model(email=email,phone=phone,name=name,gender=gender,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,phone,name,gender,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user should be staff user')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user should be superuser')
        
        return self.create_user(email,password,phone,name,gender,**extra_fields)
    
    