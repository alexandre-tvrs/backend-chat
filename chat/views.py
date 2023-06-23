from rest_framework import viewsets
from chat.models import Message
from chat.serializer import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """Exibindo todas as mensagens"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    