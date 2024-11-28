from base.base_admin import BaseAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from user.models import CustomUser

admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(BaseAdmin):
    fields = [
        "first_name",
        "last_name",
        "email",
        "profile_picture",
        "mobile_number",
        "birth_date",
        "created_at",
        "updated_at",
    ]
    list_display = ("id", "email", "created_at", "updated_at")
