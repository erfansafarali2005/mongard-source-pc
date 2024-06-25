from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from .models import Post , Comment , Vote
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostCreateUpdateForm , CommentCreateForm , CommentReplyForm , PostSearchForm
from django.utils.text import slugify
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import method_decorator

class HomeView(View):

    form_class = PostSearchForm
    def get(self , request):
        posts = Post.objects.all()
        if request.GET.get('search'): #something in the name of search is comming from url
            posts = posts.filter(body__contains=request.GET.get('search')) #now the rest of the posts will be deleted and only the searched ones remained
            #                           ^-> a field lookup
        #posts = Post.objects.order_by('body') #alphabic of body
        #posts = Post.objects.order_by('created') #creation date  old to new 
        #posts = Post.objects.order_by('-created') #new to old
        #orders can be assign in models
        return render(request , 'home/index.html' , context={'posts': posts , 'form':self.form_class})
    
class PostDetailView(View):

    template_name = 'home/detail.html'
    form_class = CommentCreateForm
    form_class_reply = CommentReplyForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post , id=kwargs['post_id'] , slug=kwargs['post_slug'])
    #       not post , we should use post_instance because post is in the same name of our model
        return  super().setup(request , *args , **kwargs)


    def get(self , request , post_id , post_slug): #now we can use *args and **kwargs instead of getting them
        #post = Post.objects.get(id=post_id , slug = post_slug)   
        #post = get_object_or_404(Post , id=post_id , slug=post_slug)
        comments = self.post_instance.pcomment.filter(is_reply = False) #pcomment = comment foreignkey to post
        return render(request , self.template_name , context={'post' : self.post_instance , 'comments':comments , 'form': self.form_class , 'reply_form' : self.form_class_reply})

    @method_decorator(login_required) # i applly login_Requesred into method decorator
    def post(self , request , *args , **kwargs): # we dont need post_id or post_slug but we  must get them so we put them into args and kwargs
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user #loginrequered is enabled so user is always loggined and is accessible from request
            new_comment.post = self.post_instance
            # we dont need is reply
            new_comment.save()
            messages.success(request , 'your comment submitted successffully' , 'success')
            return  redirect('home:post_detail' , self.post_instance.id , self.post_instance.slug)
        # ^-> we can use next url to redirect the user back to the post form the login page if he wasn't loggied

class PostDeleteView(View):

    def dispatch(self , request , *args , **kwargs):
        #post = Post.objects.get(pk=kwargs['post_id'])
        post = get_object_or_404(Post , pk=kwargs['post_id'])
        if request.user.id != post.user.id :
            messages.error(request , 'you cannot delete your post' , 'danger')
            return redirect('account:user_profile' , request.user.id)
        return super().dispatch(request, *args, **kwargs)  
    

    def get(self , request , post_id):

        try:
            Post.objects.get(pk=post_id).delete()
            messages.success(request , 'successfuly deleted' , 'success')
            return redirect('account:user_profile' , request)
        except:
            messages.error(request , 'error in deleting your post' , 'danger')
            return redirect('account:user_profile' , request.user.id) 
        


class PostUpdateView(LoginRequiredMixin , View):
    form_class = PostCreateUpdateForm
    template_name = 'home/update.html'

    def setup(self , request , *args , **kwargs):
        self.post_instance = get_object_or_404(Post , pk =kwargs['post_id'])
        return super().setup(request , *args , **kwargs)

    def dispatch( self , request , *args , **kwargs):
        post = self.post_instance
        if not request.user.id == post.user.id :
            messages.success(request , 'you cant update this post' , 'warning' )
            return redirect('account:user_profile' , request.user.id)
        return super().dispatch(request , *args , **kwargs)
    

    def get(self , request , *args , **kwargs): #we need this post_id becasue its comming from url so we useed args and kwargs
        post = self.post_instance
        form = self.form_class(instance = post)
        return render(request , self.template_name , {'form' : form})
    


    def post(self , request , *args , **kwarg): #we need this post_id becasue its comming from url so we useed args and kwargs
        post = self.post_instance
        form = self.form_class(request.POST , instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30]) # all body are now slugged
            new_post.save()
            messages.success(request , 'updated successfully' , 'success')
            return redirect('home:post_detail' , post.id , post.slug)


class PostCreateView(View):
    
    form_class = PostCreateUpdateForm
    template_name = 'home/create.html'

    def dispatch(self , request , *args , **kwargs):
        if not request.user.is_authenticated:
            messages.error(request , 'you are not loggined , please login and try again' , 'error')
            return redirect("account:user_login")
        return super().dispatch(request , *args , **kwargs)
    
    def get(self , request , *args , **kwargs):
        return render(request , self.template_name , context={'form' : self.form_class})

    def post(self , request , *args , **kwarg):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30]) # all body are now slugged
            new_post.user = request.user
            new_post.save()
            messages.success(request , 'created successfully' , 'success')
            return redirect('home:post_detail' , new_post.id , new_post.slug)


class PostAddReplyView(LoginRequiredMixin,View): # action of reply form in html in calling this url
    form_class = CommentReplyForm

    def post(self , request , post_id , comment_id):
        post = get_object_or_404(Post , pk=post_id)
        comment = get_object_or_404(Comment, pk=comment_id)

        form = self.form_class(request.POST)

        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user #loginrequered is enabled so user is always loggined and is accessible from request
            reply.post = post
            reply.reply = comment
            reply.is_reply = True
            reply.save()
            messages.success(request , 'your reply submitted successfully' , 'success')

        return redirect('home:post_detail' , post.id , post.slug)

class PostLikeView(LoginRequiredMixin,View):

    def get(self, request , *args , **kwargs):
        post = get_object_or_404(Post , pk =kwargs['post_id'])
        like = Vote.objects.filter(user=request.user, post=post)

        if like.exists():
            messages.error(request , 'your vote submitted before' , 'danger')
        else:
            Vote.objects.create(user=request.user, post=post)
            messages.success(request , 'your vote submitted successfully' , 'success')
        return redirect('home:post_detail' , post.id , post.slug)
