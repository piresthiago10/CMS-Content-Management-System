from django.contrib import admin

from contatos.models import Contato


class Contatos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'assunto', 'respondido')
    list_display_links = ('id', 'assunto')
    search_fields = ('nome', 'email', 'telefone', 'assunto')
    list_filter = ('respondido',)
    list_per_page = 10


admin.site.register(Contato, Contatos)
