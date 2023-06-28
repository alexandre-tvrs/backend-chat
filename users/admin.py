from django.contrib import admin
from django.shortcuts import redirect
from users.models import User
from admin_extra_buttons.api import ExtraButtonsMixin, button
from django.views.decorators.csrf import csrf_exempt
import csv
from django.http import JsonResponse



class Users(ExtraButtonsMixin, admin.ModelAdmin):
    @button(html_attrs={'style': 'background-color:#88FF88;color:black', 'download': "template_bulk.csv"})
    def Download(self, request):
        return redirect("http://localhost:8000/media/template_bulk.csv")

    @button(html_attrs={'style': 'background-color:#DC6C6C;color:black'})
    def Bulk(self, request):
        if request.method == 'GET':
            return redirect('/bulk/users/')

    list_display = ('id', 'nome', 'email', 'registro', 'tipo_usuario', 'id_grupo', 'img_usuario')
    list_display_links = ('id', 'nome', 'id_grupo')
    search_fields = ('nome', 'id_grupo')
    list_per_page = 20


admin.site.register(User, Users)