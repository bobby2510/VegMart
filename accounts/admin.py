from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserRegistrationForm
from .models import User,UserRole
from django.contrib.auth.models import Group
class UserAdmin(BaseUserAdmin):
    add_form=UserRegistrationForm
    list_filter=('user_role',)
    list_display=('username','email','user_role')
    search_fields=('username','email')
    ordering=('username','email')
    fieldsets=(
        (None,{'fields':('username','email')}),
        ('Permissions',{'fields':('user_role','is_admin','is_staff')}),
        ('Persional Data',{'fields':('age','gender','phone_number','last_name','first_name')}),
    )
    add_fieldsets=(
        (None,{'fields':('username','email','phone_number','password1','password2')}),
    )
    filter_horizontal=()

admin.site.register(User,UserAdmin)
admin.site.register(UserRole)
admin.site.unregister(Group)
