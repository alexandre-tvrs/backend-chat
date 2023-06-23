from django.contrib import admin
from chat.models import Message


class Messages(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'message', 'timestamp')
    list_display_links = ('id', 'user', 'group', 'message', 'timestamp')
    search_fields = ('user', 'group', 'timestamp',)
    list_per_page = 20

admin.site.register(Message, Messages)