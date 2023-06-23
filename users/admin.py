from django.contrib import admin
from users.models import User


class Users(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'senha', 'registro', 'tipo_usuario', 'id_grupo')
    list_display_links = ('id', 'nome', 'id_grupo')
    search_fields = ('nome', 'id_grupo')
    list_per_page = 20

admin.site.register(User, Users)