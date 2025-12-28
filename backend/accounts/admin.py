from django.contrib import admin
from .models import User

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display=('username', 'email', 'role', 'is_staff', 'is_superuser')
    list_filter=('role', 'is_staff', 'is_superuser')
