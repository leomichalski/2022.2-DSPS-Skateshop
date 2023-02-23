from django.db import models

# Create your models here.

class FAQ(models.Model):
    question = models.CharField(
        max_length=255,
        verbose_name='pergunta'
    )
    answer = models.TextField(
        verbose_name='resposta'
    )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'pergunta frequente'
        verbose_name_plural = 'perguntas frequentes'
