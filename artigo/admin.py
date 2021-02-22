from django.contrib import admin
from artigo.models import Artigo, Categoria


class Artigos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'categoria',
                    'data_publicacao', 'ativo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20


admin.site.register(Artigo, Artigos)


class Categorias(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Categoria, Categorias)
