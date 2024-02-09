from django.contrib import admin
from cars.admin import CarTabAdmin

from users.models import User, ServiceCompany


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'user_role', 'email']
    search_fields = ['username', 'first_name', 'user_role', 'email']

    inlines = [CarTabAdmin,]
    