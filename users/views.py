from rest_framework import viewsets
from users.models import User
from django.http import JsonResponse
from users.serializer import UserSerializer
from django.views.decorators.csrf import csrf_exempt
import csv
from django.http import HttpResponse
from django.shortcuts import redirect, render


class UsersViewSet(viewsets.ModelViewSet):
    """Exibindo todos os usuários cadastrados"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
def Bulk(request):
    if request.method == 'POST':
        content = request.FILES['file'].read().decode('utf-8')
        reader = csv.DictReader(content.splitlines(), delimiter=',')
        for row in reader:
            user = User(nome=row['nome'], email=row['email'], registro=row['registro'], tipo_usuario=row['tipo_usuario'])
            user.save()

        return redirect('/admin/users/user/')
    else:
        return render(request, 'form_bulk.html')