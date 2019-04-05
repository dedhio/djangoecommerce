from django.contrib import admin

from .models import Categoria, Servico

admin.site.register([Categoria, Servico])
