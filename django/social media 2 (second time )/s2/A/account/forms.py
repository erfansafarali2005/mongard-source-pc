from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class UserRegisterationForm(forms.Form):
    username = forms.CharField(min_length=5 , max_length=10 , widget=forms.TextInput(attrs={'class' : 'form-control' , 'palceholder' : 'your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control' , 'placeholder' : 'your email'}))
    password1 = forms.CharField(label='password' ,min_length=5 , max_length=20 , widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder' : 'your password'}) )
    password2 = forms.CharField(label='password confirm',min_length=5 , max_length=20 , widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder' : 'your password'}) )



    def clean_email(self): #email is the name of a field
        email = self.cleaned_data['email']  
        # user = User.objects.get(email=email)
        user = User.objects.filter(email=email).exists() #-> this only return True or False , we don't need the User itself
        
        if user :
            raise ValidationError('this email is already exists')
        else : 
            return email
        

    def clean(self): #if form.is_valid() won't be satisfied , it wont run the clean
        cd = super().clean() #super() : go to the form class and get cleaned_data

        p1 = cd.get('password1')
        p2 = cd.get('password2')

        if p1 and p2 and p1 != p2 :
            raise ValidationError("passwords must match ")


class UserLoginForm(forms.Form):
    username = forms.CharField(min_length=5 , max_length=10 , widget=forms.TextInput(attrs={'class' : 'form-control' , 'palceholder' : 'your username'}))
    password = forms.CharField(label='password' ,min_length=5 , max_length=20 , widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder' : 'your password'}) )
