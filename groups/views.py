from rest_framework import viewsets, generics
from groups.models import Group
from users.models import User
from chat.models import Message
from groups.serializer import GroupSerializer, AvailableGroupsSerializer, ListGroupMessagesSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os grupos cadastrados"""
    def get_queryset(self):
        queryset = Group.objects.all()
        return queryset
    serializer_class = GroupSerializer


class AvailableGroups(generics.ListAPIView):
    """Exibindo todos os grupos disponíveis"""
    queryset = Group.objects.filter(aprovado=False)
    serializer_class = AvailableGroupsSerializer



class ListGroupMessages(generics.ListAPIView):
    """Exibindo todas as mensagens do grupo"""
    def get_queryset(self):
        queryset = Message.objects.filter(group_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListGroupMessagesSerializer