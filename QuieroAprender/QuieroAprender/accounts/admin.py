from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_authenticated",
        "is_superuser",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["username", "email"]
    search_fields = ["username", "email", "first_name", "last_name"]

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("bio", "profile_photo", "birth_date")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("bio", "profile_photo", "birth_date")}),
    )
