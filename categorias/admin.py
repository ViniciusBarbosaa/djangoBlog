from django.contrib import admin
from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cat')
    list_display_link = ('id', 'nome_cat')

admin.site.register(Categoria, CategoriaAdmin)