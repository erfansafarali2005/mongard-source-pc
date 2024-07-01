from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from .forms import UserRegisterationForm  , UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Post
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .models import Relation

class UserRegisterView(View):

    form_class = UserRegisterationForm
    template_name = 'account/register.html'

    def dispatch(self , request , *args , **kwargs):
        if request.user.is_authenticated :
            messages.error(request , 'you are already loggined' , 'danger')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
        
    

    def get(self , request):
        form = self.form_class()
        return render (request , self.template_name , context={'form' : form})

    def post(self , request):
            form = self.form_class(request.POST)

            if form.is_valid():
                cd = form.cleaned_data
                User.objects.create_user(username=cd['username'] , password=cd['password1']) #these are form names
                messages.success(request , 'you registered successfulyy' , 'success')
                return redirect('home:home')
            else :
                 return render(request , self.template_name , {"form" : form}) #if there was a problem in form filling , -> <form ... novalidate>
                    


class UserLoginView(View):

    form_class = UserLoginForm
    template_name = 'account/login.html'

    def setup(self , request , *args , **kwargs):
        #                         ^-> get from dictionary : if exists , if not -> None
        self.next = request.GET.get('next' , None) #sm is comming from the url in the name of next if not exists , return None
        return super().setup(request , *args , **kwargs)


    # !!!! see profile is loginreqaueredmixin , when someone click on the others profile , it redirects into login so we dont want that
    # now we check if there was any next , redirect it to the next , if it wasn't just go on !

    def dispatch(self , request , *args , **kwargs):
        if request.user.is_authenticated :
            messages.error(request , 'you are already loggined' , 'danger')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)    

    def get(self , request):
        form= self.form_class()
        return render(request , self.template_name , context={'form':form})
        
    def post(self , request):
        form = self.form_class(request.POST)    
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request , username=cd['username'] , password=cd['password']) #now email can also be sent into username field
            if user is not None:
                login(request , user)
                messages.success(request , 'you logged in successfully' , 'success')
                #return redirect('home:home')
                if self.next : #if he was redirected to login like following without being loggined ?
                    return redirect(self.next)
                else :  #if it was normall login
                    redirect('account:user_profile' , user.id)
            else :
                 messages.error(request , 'username or password is wrong' , 'warning')

        return render(request , self.template_name , context={'form' : form})        
    

class UserLogoutView(LoginRequiredMixin,View):
    #LOGIN_URL='/account/login.html' #here or in the setting.py
    def get(self , request):
        logout(request)    
        messages.success(request , 'you loggged out successfulyy' , 'success')
        return redirect ('home:home')
    

class UserProfileView(LoginRequiredMixin ,View):

    template_name = 'account/profile.html'

    def get(self , request , user_id):
        is_following = False
        #user = User.objects.get(pk=user_id)
        user = get_object_or_404(User , pk=user_id)
        #posts = Post.objects.filter(user=user) #post object is not iterable {% for post in posts %}
        posts = user.posts.all() #posts is the related_name in model which has backward relation querying
        #we cant use get_list_or_404 becasue there maybe a user without any posts
        relation = Relation.objects.filter(from_user = request.user , to_user = user.id)
        if relation.exists():
            is_following = True

        return render(request , self.template_name , context={'user':user , 'posts':posts , 'is_following' : is_following})
    

#### !!! if user email exists or not in the datagbase , it sends the email link ! becasue hacker may come and test different emails !!! ####    

class UserPasswordResetView(auth_views.PasswordResetView): #view is handeled by django
    template_name = 'account/password_reset_form.html' #the template
    success_url = reverse_lazy('account:password_reset_done') #after that email is sent
    email_template_name = 'account/password_reset_email.html' #the context if the email

class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'account/password_reset_done.html' # template of the page after that email is sent


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView): #after the client's password is changed successfully
    template_name = 'account/password_reset_complete.html' #the template of success password change


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView): #the page that user enters its new password 
    template_name ='account/password_reset_confirm.html' #its template
    success_url = reverse_lazy('account:password_reset_complete') # the url of the page that you successfully changed your password


class UserFollowView(LoginRequiredMixin , View):
 
    def get(self , request , user_id):
        user = User.objects.get(id = user_id)
        relation = Relation.objects.filter(from_user = request.user , to_user = user)

        if relation.exists():
            messages.error(request , 'you are already following this user' , 'info')
        else:
            Relation.objects.create(from_user = request.user , to_user = user) 
            #Relation(from_user = request.user , to_user = user).save() 
            messages.success(request , 'you followed this user' , 'success')   
        return redirect('account:user_profile' , user.id)   
        


class UserUnfollowView(LoginRequiredMixin , View):


    def get(self , request , user_id):
        user = User.objects.get(id = user_id)
        relation = Relation.objects.filter(from_user = request.user , to_user = user)

        if relation.exists():
            relation.delete()
            messages.success(request , 'you unfollowed this user ' , 'success')
        else : 
            messages.error(request , 'you are not following this user' , 'danger')
        return redirect('account:user_profile' , user.id)    



