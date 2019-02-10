from django import forms
from django.contrib import admin

from .models import User


class UserAdmin(UserAdmin):
    search_fields = ['email', ]
    list_display = ('email', 'is_staff', 'is_superuser', 'created_at')
    ordering = ('-created_at',)


admin.site.register(User, UserAdmin)
