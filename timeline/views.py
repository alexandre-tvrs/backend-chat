from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets, generics
from timeline.models import Task
from groups.models import Group

@csrf_exempt
def create(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        dataEntrega = request.POST.get('dataEntrega')
        group_id = request.POST.get('group_id')

        group = Group.objects.filter(id = group_id).first()

        task = Task(titulo = titulo, descricao = descricao, dataEntrega = dataEntrega, group = group)
        task.save()

        return JsonResponse({'status': 'cadastrado'})