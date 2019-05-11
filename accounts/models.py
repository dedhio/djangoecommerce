import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin, BaseUserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Apelido / Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um usuário válido. '
                'Este valor deve ter apenas letras, numeros '
                'e os caracteres: @ . + - _ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo'
    )
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(' ')[0]

