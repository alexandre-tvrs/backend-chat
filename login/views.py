from django.http import JsonResponse
from login.models import Login
from users.models import User
from django.views.decorators.csrf import csrf_exempt
import random


@csrf_exempt
def verificaLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(email=email).first()
        if user is None:
            return JsonResponse({'status': 'usuário não encontrado'})

        login = Login.objects.filter(user=user).first()

        if email == user.email and senha == login.senha:
            hash = random.getrandbits(128)
            return JsonResponse({'status': 'Login efetuado com sucesso', 'id': login.user.id, 'token': hash})
        else:
            return JsonResponse({'status': 'Usuário e/ou senha incorretos'})
    else:
        return JsonResponse({'status': 'Método errado!'})
    

@csrf_exempt
def criaLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(email=email).first()
        if user is None:
            return JsonResponse({'status': 'usuário não encontrado'})

        login = Login.objects.filter(user=user).first()

        if login is None:
            login = Login(user=user, senha=senha)
            login.save()
            return JsonResponse({'status': 'Usuário criado com sucesso'})
        else:
            return JsonResponse({'status': 'Login já existe'})
    else:
        return JsonResponse({'status': 'Método errado'})