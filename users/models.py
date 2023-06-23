from django.db import models

class User(models.Model):
    TIPO = (
        (1, 'Aluno'),
        (2, 'Professor'),
    )
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    registro = models.CharField(max_length=50)
    tipo_usuario = models.IntegerField(choices=TIPO, null=False, default=1)
    id_grupo = models.ForeignKey('groups.Group', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
    