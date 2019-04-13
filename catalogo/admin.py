from django.contrib import admin

from .models import Categoria, Servico


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created', 'modified', 'categoria', 'preco']
    search_fields = ['name', 'slug', 'categoria__name']
    list_filter = ['created', 'modified']


