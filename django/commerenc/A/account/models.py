from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(unique=True , max_length=255)
    phone_number = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager() #managing and quering on objects -> User.objects.create ...

#   ^-> we used to write a new authentication system before for autherozing with email too ,  but now ...
    USERNAME_FIELD = 'phone_number' #the username field can be also authenticates with eamil  | everyfields inside USERNAME_FIELD must be unique
    REQUIRED_FIELDS = ['email' , 'full_name']          #only avaible in superuser

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label): #app_label is the name of the app
        return True

    @property #property becasue django dosn't put () ahead of it
    def is_staff(self):
        return self.is_admin #this was a Boolean Field which will be returned as the result



class OTPCode(models.Model):
    phone_number = models.CharField(max_length=12, unique=True) #we could use foreignkey , but first this model will be executed
    code = models.PositiveSmallIntegerField(unique=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'

