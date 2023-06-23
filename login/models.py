from django.db import models


class Login(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.user.email