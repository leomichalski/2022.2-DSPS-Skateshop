# Generated by Django 3.2.4 on 2023-02-23 16:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20230223_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='may_be_in_homepage',
        ),
        migrations.AddField(
            model_name='product',
            name='is_in_homepage',
            field=models.BooleanField(default=True, verbose_name='aparece na home'),
        ),
        migrations.AlterField(
            model_name='category',
            name='homepage_priority',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='prioridade na home (quanto maior, mais em cima)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_in_homepage',
            field=models.BooleanField(default=False, verbose_name='está na home?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='limitedtimeoffer',
            name='absolute_discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='desconto absoluto (R$)'),
        ),
        migrations.AlterField(
            model_name='limitedtimeoffer',
            name='end_datetime',
            field=models.DateTimeField(verbose_name='término da promoção'),
        ),
        migrations.AlterField(
            model_name='limitedtimeoffer',
            name='relative_discount',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(95)], verbose_name='desconto relativo (%)'),
        ),
        migrations.AlterField(
            model_name='limitedtimeoffer',
            name='start_datetime',
            field=models.DateTimeField(verbose_name='início da promoção'),
        ),
        migrations.AlterField(
            model_name='product',
            name='base_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='preço base (ou seja, sem promoção)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category', verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='no_image.jpg', help_text='Proporção recomendada: 1:1 (quadrada).', upload_to='products', verbose_name='imagem'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='está disponível'),
        ),
        migrations.AlterField(
            model_name='product',
            name='limited_time_offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.limitedtimeoffer', verbose_name='promoção'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
    ]
