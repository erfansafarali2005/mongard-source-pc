from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    #                                                           ^-> now we dont need _set to use backward_relation -> user.posts
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name = 'posts') #one to few relation 
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)


    class Meta : #meta options
        ordering = ('-created','body') #now order of  queries are alphabic or etc ... | if created was same , use alphabic ordering


    def __str__(self):
        return f'{self.user} - {self.slug} - {self.created}'
    

    def get_absolute_url(self):
        return reverse('home:post_detail' , args=(self.id , self.slug))
    
    def likes_count(self): # self is pointing to the post that now user is watching (visited one)
        return self.pvotes.count() #pvote is the related name of Vote
    
class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name = 'ucommnets')
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name = 'pcomment')
    #                                                                                                             ^-> in database it can be empty
    reply = models.ForeignKey('Comment' , on_delete=models.CASCADE , related_name = 'rcomments' , blank=True , null=True) #maybe its not reply so its empty
    #                                                                                                ^-> in forms it can be empyu
    is_reply = models.BooleanField(default = False)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'



class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name = 'uvote')
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name = 'pvotes')

    def __str__(self):
        return f'{self.user} liked  - {self.post.slug}'