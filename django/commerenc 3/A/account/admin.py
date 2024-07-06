from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm , UserCreationForm
from .models import User , OTPCode
from django.contrib.auth.models import Group


@admin.register(OTPCode)
class OTPCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number','code' , 'created')
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone_number' ,'is_admin')
    list_filter = ('is_admin',) #a check to filter only admins
    fieldsets = (
        (None, {'fields': ('email', 'phone_number' , 'full_name' , 'password')}), #these are normanl fields without grouping
        ('Permissions', {'fields': ('is_active', 'is_admin' , 'last_login')}), #premission collumn contains these fields
    )

    add_fieldsets = ( #fields which we add datas to them
        (None , {'fields': ('email', 'phone_number' , 'full_name' , 'password1' , 'password2')}),

    )

    search_fields = ('email', 'phone_number')
    ordering = ('full_name',)
    filter_horizontal = ()

admin.site.register(User , UserAdmin)
admin.site.unregister(Group)#unregister these models to register the main custom User and Adminuser fields

