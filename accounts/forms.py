from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField

from .models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'username')


class UserAdminChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'nome', 'username', 'is_active', 'is_staff')

