from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterationForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label= 'password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}))


  #!!!!these functions automaticlly run when they are called by is_valid()!!!!

    def clean_email(self): #clean is django specified and email is my email field in UserRegisterationForm class
        email = self.cleaned_data['email'] #cleaned data coming from the sub class (UserRegisterationForm) -> ['email']
        user = User.objects.filter(email = email).exists()
        if user :
            raise ValidationError ("this email is already exists ")
        return email #the filed must be returned


    def clean(self): #overwriting clean
        cd = super().clean() #super gatters everything in cleaned data

        p1 = cd.get('password1') #password1 and 2 are our field names
        p2 = cd.get('password2') # ^

        if p1 and p2 and p1 != p2:
            raise ValidationError('passwords are not equals')





class UserLoginForm(forms.Form): #the login from of the login page
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))