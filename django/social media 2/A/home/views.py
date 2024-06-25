from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PostCreateUpdateForm
from django.utils.text import slugify

class HomeView(View):
    template_name = 'index.html'
    def get(self,request):
        posts = Post.objects.all()
        return render(request, self.template_name , {'posts' : posts})



class PostDetailView(View):

    template_name = 'detail.html'

    def get(self , request , post_id , post_slug):
        post = get_object_or_404(Post , pk = post_id , slug = post_slug)
        return render(request , self.template_name , {'post' : post})




class PostDeleteView(LoginRequiredMixin,View):

    def get(self , request , post_id):
        post = get_object_or_404(Post , pk = post_id )
        if post.user.id == request.user.id:
        #  ^-> owner of post| ^-> owner of login
            post.delete()
            messages.success(request , 'deleted succesfully ' , 'success')
        else:
            messages.error(request , 'pleaes login first you are not the owner of the selected post' , 'danger')
        return redirect('home:home')
    #    ^-> lastly it will be executed



class PostUpdateView(LoginRequiredMixin , View):
    form_class = PostCreateUpdateForm
    template_name = 'update.html'

    #***why not to use post_instacne as a class variable ? -> class variables will be excuted when the class is imported***
    def setup(self, request , *args , **kwargs): #setup -> for preventing doing oprations on and on !
        self.post_instance = get_object_or_404(Post , pk=kwargs['post_id']) #now we open the database once only !
        #                    get_objects.order_by('body') -> it works as get_all but with alphabic order
        #                    get_objects.order_by('-body') -> it works as get_all but with reverse alphabic order
        #                    get_objects.order_by('?') -> it works as get_all but with random order -> takes too much cpu !
        return super().setup(request , *args , **kwargs)

    def disptach(self , request , *args , **kwargs): #!!! after being runned , the data inside it is not accessible but setup is
        post = self.post_instance #see setup fuction
        #                           ^->everything coming from outside will be stored as a dictionary in **kwargs
        if not post.user.id == request.user.id:
            messages.error(request , 'you only can update your owned posts' , 'danger')
            return redirect ('home:home')
        return super().dispatch(request , *args , *kwargs) # -> we continue the opration with super and lending forwards the args and kwargs

    def get(self, request , post_id , *args , **kwargs):
        post = self.post_instance #see setup fuction
        form = self.form_class(instance = post)
        return render(request , self.template_name , {'form':form})

    def post(self, request, post_id , *arsg , **kwargs):
        post = self.post_instance #see setup fuction
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            new_form = form.save(commit=False) #commit = False -> it won't save (commit) it
            #you can do whatever you want to do here then save it
            new_form.save()
            messages.success(request , 'updated successfully' , 'success')
            return redirect('home:post_detail' , post.id , post.slug)




class PostCreateView(LoginRequiredMixin , View):
    template_name = 'create.html'
    form_class = PostCreateUpdateForm

    def get(self , request):
        form = self.form_class
        return render(request , self.template_name , {'form':form})


    def post(self , request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:30])
            new_post.user = request.user
            new_post.save() #only needs required fields (slug and user) , datetimes are all auto_on_add(True) ->manually
            messages.success(request , 'post created' , 'success')
            return redirect ('home:post_detail' , new_post.id , new_post.slug)
