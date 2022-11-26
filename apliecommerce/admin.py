
from django.contrib import admin
from apliecommerce.models import *

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
