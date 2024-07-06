from django.shortcuts import render , redirect
from django.views import View
from .forms import  UserRegisterationForm
import random
from utils import send_otp_code
from .models import OTPCode , User
from django.contrib import messages
from .forms import VerifyCodeForm
class UserRegisterView(View):

    from_class = UserRegisterationForm
    template_name = 'account/register.html'
    def get(self, request):
        form = self.from_class
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.from_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000 , 9999)
            send_otp_code(form.cleaned_data['phone_number'] , random_code)
            OTPCode.objects.create(phone_number = form.cleaned_data['phone_number'], code = random_code)
            request.session['user_registeration_info'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email' : form.cleaned_data['email'],
                'full_name' : form.cleaned_data['full_name'],
                'password' : form.cleaned_data['password'],
            }

            messages.success(request, 'we sent you a code' , 'success')
            return redirect('account:verify_code')
        return redirect('home:home')

class UserRegisterVerifyCodeView(View):
    template_name = 'account/verify_code.html'
    form_class = VerifyCodeForm
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user_session = request.session['user_registeration_info']
        code_instance = OTPCode.objects.get(phone_number = user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data #        ^-> code field in OTP_code

            if int(cd['code']) == code_instance.code:
                User.objects.create_user(user_session['phone_number'] , user_session['email'] , user_session['full_name'],
                                         user_session['password']
                                         )
                code_instance.delete()
                messages.success(request , 'you registered successfully' , 'success')
                return redirect('home:home')

            else:
                messages.error(request , 'wrong OTP code' , 'danger')
                return redirect('account:verify_code')

        return render(request , self.template_name , {'form': form})