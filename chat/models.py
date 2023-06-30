from django.db import models


class Message(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=200)
    #image = ResizedImageField(force_format='WEBP', size=None, scale=0.5, quality=75, upload_to='images', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    