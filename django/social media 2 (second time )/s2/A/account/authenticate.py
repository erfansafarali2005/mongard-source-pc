from django.contrib.auth.models import User

# aval username ro mizare to username ba authentication defaultesh bad ino yani email ro mikone to username

class EmailBackend:
#                                         *User fields*
    def authenticate(self , request , username=None , password=None): #editing authenticate(username=cd[...])
        #user = User.objects.get(username=username) -> default
        try:
            user = User.objects.get(email = username) #usernamefield can also be filled with email | user filled the emailfield with the field in the name of username with email so this funciton works . if it was username , default authentication system ran
            #                                 ^-> usernamefield which is filled with email instead | default check email so it dosn't work so this works isntead
            if user.check_password(password):
                return user #return user to user variable in views.py
            else:
                return None    # if user is not None : 
        except User.DoesNotExist:
            return None     

    def get_user(self , user_id):
        try :
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None