from django.db import models

def upload_arquive_task(instance, filename):
    return f'{instance.group}/{instance.titulo}/{filename}'

class Task(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to=upload_arquive_task, null=True, blank=True)
    dataEntrega = models.DateField()
    entregue = models.BooleanField(default=False)
    comentario = models.CharField(max_length=200, null=True, blank=True)
    entregueBy = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, related_name='tasks')
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, null=True, blank=True, related_name='timelines')
