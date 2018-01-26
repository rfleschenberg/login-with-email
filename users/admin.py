from django import forms
from django.contrib import admin

from .models import User


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password', 'is_staff', 'is_superuser',
                  'last_login', 'groups', 'user_permissions', ]
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm


admin.site.register(User, UserAdmin)
