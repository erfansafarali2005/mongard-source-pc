from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from .forms import UserRegisterationForm , UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Post
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy

class RegisterView(View):

    def dispatch(self ,request, *args , **kwargs): #dispatch runs before request to be sent to post and get (it is now overwritten)
        if request.user.is_authenticated :
            return redirect ("home:home") # we can even design a page for this type of error
        return super().dispatch(request , *args , **kwargs) #this leads the programm to conitunue its proccess

    form_class = UserRegisterationForm

    def get(self,request): #self.form_class() as form_class
        form = self.form_class()
        return render(request, 'account/register.html' , {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid(): #custom validation in form.py
            cd = form.cleaned_data
            User.objects.create_user(cd['username'] , cd['email'], cd['password1'])
            messages.success(request , 'user created successfully ' , 'success')

        #if user is not valid -> forms.py functions will work
        return render(request , 'account/register.html' , {'form' :form})



class  UserLoginView(View):

    def dispatch(self ,request, *args , **kwargs): #checkes if user is already loggined just before going to post and get
        if request.user.is_authenticated :
            return redirect ("home:home")
        return super().dispatch(request , *args , **kwargs)
    
    form_class = UserLoginForm
    template_name = 'account/login.html' # we can use this methond to prevent writing extra codes in rerturns

    def get(self, request):
          form = self.form_class #
          return render (request , 'account/login.html' , {'form':form})

    def post(self, request):
           form = self.form_class(request.POST)
           if form.is_valid():
               cd = form.cleaned_data
               user = authenticate(request , username = cd['username'] , password = cd['password']) #query sets wont start processing until they are used like the below line
               if user is not None: #it returns none if it can't authenticate the data / now the query command will be ran (not in the upper line ^)
                   login(request , user ) #only needs request ( to recieve the curently loggined user ) and the User
                   messages.success(request , 'loggined successfully' , 'success')
                   return redirect ('home:home')

               else:
                   messages.error(request , 'username or password is wrong' , 'danger')

           return  render (request , self.template_name , {'form':form})


class UserLogoutView(LoginRequiredMixin,View):
 login_url = '/account/login' #logn_url -> it says to django to redirect the user to this login_url (if you dont write -> it redirects it to another url)



 def get(self , request):
        logout(request) #only need the request to logout the curently logined user
        messages.success(request , 'loggouted successfully' , 'success')
        return redirect ('home:home')



class UserProfileView(LoginRequiredMixin , View):
    template_name = 'account/profile.html'
    def get(self , request ,  user_id):
        user = get_object_or_404(User , pk = user_id ) #pk = id (priamry key collumn of the model)
        posts = Post.objects.filter(user=user) #cannot use get_list_or_404 -> if the user dosn't have any post it dosn't show the empty profile and returns 404
    #   |-> user = user -> user in models = user which comes from pk=user_id
        return render(request , self.template_name , {'user' : user , 'posts' : posts})




class UserPasswordResetView (auth_view.PasswordResetView): #the form of the class
    template_name = 'account/password_reset_form.html' #the template name
    success_url = reverse_lazy('account:password_reset_done') #the page which it says : email is sent
    email_template_name ='account/password_reset_email.html' #the email which is sent


class UserPasswordResetDoneView(auth_view.PasswordResetDoneView): #the form which says : email is sent
    template_name = 'account/password_reset_done.html'


class UserPasswordResetConfirmView(auth_view.PasswordResetConfirmView): #the form which user types its new password
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')

class UserPasswordResetCompleteView(auth_view.PasswordResetCompleteView): # the form which says : you have changed your password successfully
    template_name = 'account/password_reset_complete.html'