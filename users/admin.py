from django import forms
from django.contrib import admin

from .models import User


class UserAdminForm(forms.ModelForm):

    password = forms.CharField(required=False, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'password', 'is_staff', 'is_superuser',
                  'last_login', 'groups', 'user_permissions', ]
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm


admin.site.register(User, UserAdmin)
