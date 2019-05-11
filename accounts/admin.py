from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserAdminChangeForm, UserAdminCreationForm


class UserAdmin(BaseUserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['username', 'nome', 'email', 'is_active', 'is_staff', 'date_joined']
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
    )
    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        ('Informacoes pessoais', {'fields': ('nome', 'last_login')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )


admin.site.register(User, UserAdmin)
