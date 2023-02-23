from django.db import models
from model_utils.models import TimeStampedModel


class Company(TimeStampedModel):
    name = models.CharField(
        max_length=64,
        verbose_name='nome'
    )
    insta = models.CharField(
        max_length=32,
        verbose_name='instagram'
    )
    youtube = models.CharField(
        max_length=70,
        verbose_name='youtube'
    )
    email = models.CharField(
        max_length=32,
        verbose_name='email'
    )
    phone = models.CharField(
        max_length=16,
        verbose_name='celular'
    )
    business_hours = models.CharField(
        max_length=64,
        verbose_name='horário de Funcionamento'
    )
    address = models.CharField(
        max_length=150,
        verbose_name='endereço'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'dados da empresa'
        verbose_name_plural = 'dados da empresa'
