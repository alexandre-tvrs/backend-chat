from rest_framework import viewsets, generics
from groups.models import Group
from users.models import User
from chat.models import Message
from groups.serializer import GroupSerializer, ListUsersGroupSerializer, ListGroupMessagesSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os grupos cadastrados"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ListUsersGroups(generics.ListAPIView):
    """Lista de todos os usuários no grupo"""
    def get_queryset(self):
        queryset = User.objects.filter(id_grupo=self.kwargs['pk'])
        return queryset
    serializer_class = ListUsersGroupSerializer


class ListGroupMessages(generics.ListAPIView):
    """Exibindo todas as mensagens do grupo"""
    def get_queryset(self):
        queryset = Message.objects.filter(group_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListGroupMessagesSerializer