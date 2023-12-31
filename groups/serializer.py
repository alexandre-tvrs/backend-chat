from rest_framework import serializers
from users.serializer import UserSerializer
from groups.models import Group
from users.models import User
from chat.models import Message
from timeline.models import Task


class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ['id', 'nome', 'descricao', 'id_professor', 'aprovado', 'img_group', 'users']    
    

class ListGroupMessagesSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Message
        fields = ['user', 'message']
    def get_user(self, obj):
        return obj.user
        
class ListTimelineSerializer(serializers.ModelSerializer):
    entregueBy = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'titulo', 'dataEntrega', 'arquivo', 'entregue', 'comentario', 'entregueBy', 'descricao', 'group']
    def get_entregueBy(self, obj):
        return obj.entregueBy.nome