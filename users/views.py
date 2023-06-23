from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.serializer import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    """Exibindo todos os usuários cadastrados"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
