# Generated by Django 3.2.4 on 2023-02-15 21:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='banners/')),
                ('photo_alt', models.CharField(blank=True, max_length=300, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('is_in_homepage', models.BooleanField(default=True)),
                ('homepage_priority', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
                'ordering': ('homepage_priority',),
            },
        ),
    ]
