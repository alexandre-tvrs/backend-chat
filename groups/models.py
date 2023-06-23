from django.db import models


class Group(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    id_professor = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'tipo_usuario': 2})
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
