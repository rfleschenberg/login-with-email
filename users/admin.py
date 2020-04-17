from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    search_fields = ['email', ]
    list_display = ('email', 'is_staff', 'is_superuser', 'created_at')
    ordering = ('-created_at',)


admin.site.register(User, UserAdmin)
