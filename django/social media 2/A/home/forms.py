from django import forms
from .models import Post


class PostCreateUpdateForm (forms.ModelForm): #the form of the post_update
    class Meta: #Meta is used to creates a form from another model (Post model)
        model = Post
        fields = ("body",)
        #               ^-> hifen needed