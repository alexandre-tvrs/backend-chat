from rest_framework import serializers
from groups.models import Group
from users.models import User
from chat.models import Message
from timeline.models import Task


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'nome', 'descricao', 'id_professor', 'aprovado']


class ListUsersGroupSerializer(serializers.ModelSerializer):
    tipo_usuario = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'nome', 'tipo_usuario']
    def get_tipo_usuario(self, obj):
        return obj.get_tipo_usuario_display()
    

class ListGroupMessagesSerializer(serializers.ModelSerializer):
    nome = serializers.SerializerMethodField()
    class Meta:
        model = Message
        fields = ['nome', 'message']
    def get_nome(self, obj):
        return obj.user.nome
    
class ListTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'titulo', 'dataEntrega', 'entregue', 'descricao', 'group']