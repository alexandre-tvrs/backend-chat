from rest_framework import viewsets, generics
from groups.models import Group
from users.models import User
from chat.models import Message
from groups.serializer import GroupSerializer, ListGroupMessagesSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os grupos cadastrados"""
    def get_queryset(self):
        queryset = Group.objects.all()
        aprovado = self.request.query_params.get('aprovado')
        professor = self.request.query_params.get('professor')
        if aprovado:
            queryset = queryset.filter(aprovado=aprovado)

        if professor:
            queryset = queryset.filter(id_professor=professor)

        return queryset
    serializer_class = GroupSerializer


class ListGroupMessages(generics.ListAPIView):
    """Exibindo todas as mensagens do grupo"""
    def get_queryset(self):
        queryset = Message.objects.filter(group_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListGroupMessagesSerializer