from django.contrib import admin
from groups.models import Group


class Groups(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'id_professor', 'aprovado', 'img_group')
    list_display_links = ('id', 'nome', 'id_professor', 'aprovado')
    search_fields = ('nome', 'aprovado',)
    list_per_page = 20

admin.site.register(Group, Groups)