from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("uuid", "username","password","email")
    search_fields = ("username",)
    list_filter = ("username",)