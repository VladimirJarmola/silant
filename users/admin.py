from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from cars.admin import CarTabAdmin
from users.models import User
from users.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ['username', 'first_name', 'user_role', 'email']
    search_fields = ['username', 'first_name', 'user_role', 'email']

    ordering = ['username',]

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'user_role')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'user_role',)}
        ),
    )

    inlines = [CarTabAdmin,]

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.user_role == "SE":
            return []
        return ['service_company']

    

admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):

#     list_display = ['username', 'first_name', 'user_role', 'email']
#     search_fields = ['username', 'first_name', 'user_role', 'email']
    
#     inlines = [CarTabAdmin,]
    
    # def get_readonly_fields(self, request, obj=None):
    #     if obj and obj.user_role == "SE":
    #         return ['password']
    #     return []