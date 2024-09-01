from django import forms
from .models import User , OTPCode
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email' , 'phone_number' , 'full_name') #here we are saving these forms but not the password

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('Passwords must match')
        return cd['password2'] #its returned to be passed through other proccess

    def save(self, commit=True):
        user = super().save(commit=False) #the save in the models.py is now retunred here so there is a user inside
        user.set_password(self.cleaned_data['password2'])
        if commit: #when in views you put commit=True
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(help_text="use cant change password using <a href='\"../password/\'>this form</a>")

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name' , 'password' , 'last_login') # last_login is a bulit_in field from AbstractBaseFolder



class UserRegisterationForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(widget=forms.TextInput())
    phone_number = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()

        if user :
            raise ValidationError('Email already registered')
        else :
            return email

    def clean_phone(self):
        phone = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone).exist()


        if user :
            raise ValidationError('Phone number already registered')
        OTPCode.objects.filter(phone_number = phone).delete()
        return phone


class VerifyCodeForm(forms.Form):
    code = forms.CharField()


class UserLoginForm(forms.Form):
    phone = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)