from django.contrib.auth.models import User

class Emailbackend:
    def authenticate(self , request , username = None , password =None): #authenticate is a def which does the authentication stuffs
    #                                 this username and password is which sent from authenticating (not specefic username and password) we just need to get them
        try : #use try except when you want to know something is exists or not
            user = User.objects.get(email=username) #we get the user and search username in email field / defualtly -> username = username ->username = cd["username"]
            if user.check_password(password): #if the password was correct
                return user #return user to the -> views.py/-> if user is not None
            return None

        except User.DoesNotExist:
          return None




    def get_user(self, user_id): #to get the user with user_id
        try:
           return User.objects.get(pk=user_id) #pk = pirmary key -> it searchs for the primary key now

        except User.DoesNotExist:
            return None
