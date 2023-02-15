from django.db import models
from django.conf import settings


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class FileModel(models.Model):
    file = models.FileField(upload_to='files/')
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=64, null=False, default="Patrocinado")

    active = ActiveManager()

    def __str__(self):
        return self.file.name
