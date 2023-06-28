from rest_framework import serializers
from users.serializer import UserSerializer
from groups.models import Group
from users.models import User
from chat.models import Message


class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ['id', 'nome', 'descricao', 'id_professor', 'aprovado', 'img_group', 'users']    
    

class ListGroupMessagesSerializer(serializers.ModelSerializer):
    nome = serializers.SerializerMethodField()
    class Meta:
        model = Message
        fields = ['nome', 'message']
    def get_nome(self, obj):
        return obj.user.nome