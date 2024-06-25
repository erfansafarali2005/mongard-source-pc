from django.db import models
from django.shortcuts import reverse


from django.contrib.auth.models import User



class Post (models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE) #Foreignkey is connecttion between other models
    #^-> must get an object of user in views -> request.user (can be an object of user for instance)
    body = models.TextField()
    slug = models.SlugField() # slug = http:///google.com/posts/3/django-tutorial
                                                                     #^^
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True) #auto_now_add : adds the realtime , date and time

    class Meta:
        ordering = ['-created' , 'body']

    def __repr__(self): #__repr__ : when class is represented like the post list in admin panel it shows the object name but what __repr__ returns will be shown
        return f"{self.slug} - {self.updated}"

    def get_absolute_url(self):
        return reverse('home:post_detail' , args=[self.id , self.slug])