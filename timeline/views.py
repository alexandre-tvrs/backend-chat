from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets, generics
from timeline.models import Task
from users.models import User
from groups.models import Group

@csrf_exempt
def createTask(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        dataEntrega = request.POST.get('dataEntrega')
        group_id = request.POST.get('group_id')

        group = Group.objects.filter(id = group_id).first()

        task = Task(titulo = titulo, descricao = descricao, dataEntrega = dataEntrega, group = group)
        task.save()

        return JsonResponse({'status': 'cadastrado'})
    

@csrf_exempt
def updateTask(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        arquivo = request.FILES.get('arquivo')
        entregueBy = request.POST.get('entregueBy')
        comentario = request.POST.get('comentario')

        task = Task.objects.filter(id = id).first()
        user = User.objects.filter(id = entregueBy).first()
        task.arquivo = arquivo
        task.entregueBy = user
        task.comentario = comentario
        task.entregue = True
        task.save()

        return JsonResponse({'status': 'atualizado'})