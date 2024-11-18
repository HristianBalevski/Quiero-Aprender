from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    list_display = ['username', 'email', 'first_name', 'last_name', 'birth_date', 'is_staff', 'is_active']


    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'profile_photo', 'birth_date')}),
    )


    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio', 'profile_photo', 'birth_date')}),
    )


    add_form = UserAdmin.add_form
    form = UserAdmin.form


admin.site.register(CustomUser, CustomUserAdmin)
