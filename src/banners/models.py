from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Banner(models.Model):
    photo = models.ImageField(
        upload_to='banners/',
        help_text='Resolução recomendada: 1920x600.',
        verbose_name='foto'
    )
    photo_alt = models.CharField(
        max_length=300, blank=True, null=True,
        verbose_name='texto alternativo da foto'
    )
    link = models.URLField(
        blank=True, null=True,
    )
    # TODO: change title max length
    title = models.CharField(
        max_length=64, blank=True, null=True,
        verbose_name='título'
    )
    # TODO: change decription max length
    description = models.CharField(
        max_length=300, blank=True, null=True,
        verbose_name='descrição'
    )
    is_in_homepage = models.BooleanField(
        default=True,
        verbose_name='está na home?'
    )
    homepage_priority = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='prioridade na home (maior = primeiro)'
    )

    class Meta:
        ordering = ('homepage_priority',)
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

    def __str__(self):
        return self.photo.name

