from django import forms

class UserRegisterationForm(forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()