from django.contrib import admin
from .models import User, Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("uuid", "username","password","email")
    search_fields = ("username",)
    list_filter = ("username",)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("bio", "avatar","birth_date","phone_number")