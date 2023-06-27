from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    dataEntrega = models.DateField()
    entregue = models.BooleanField(default=False)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, null=True, blank=True, related_name='timelines')
