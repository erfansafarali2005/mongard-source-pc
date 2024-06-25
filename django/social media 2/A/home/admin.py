from django.contrib import admin
from .models import Post



@admin.register(Post) #custome admin panel with Post model
class PostAdmin(admin.ModelAdmin): #every custome admin panel should inherits fromn admin.ModelAdmin
    list_display = ('user' , 'slug' , 'updated') #changes the list collumn of models
    search_fields = ('slug','body') #adds a search box with the matteriasl of slug and body
    list_filter = ('updated',) #filter the list of users with updated field (in model) !!!!!!!should add a (,) after the last item !!!!!
    raw_id_fields = ('user',) #the user drop menu now its not avaible and you should write the user_id manually !!!!!!!should add a (,) after the last item !!!!!

#admin.site.register(Post , PostAdmin) -> we can use the @admin.register(mymodel) instead and then write the class after it
