from django.db import models


def upload_image_group(instance, filename):
    return f'{instance.nome}/{filename}'

class Group(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    id_professor = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'tipo_usuario': 2})
    img_group = models.ImageField(upload_to=upload_image_group, null=True, blank=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
