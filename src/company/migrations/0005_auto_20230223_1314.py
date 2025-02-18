# Generated by Django 3.2.4 on 2023-02-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_company_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='company',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=150, verbose_name='endereço'),
        ),
        migrations.AlterField(
            model_name='company',
            name='business_hours',
            field=models.CharField(max_length=64, verbose_name='horário de Funcionamento'),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.CharField(max_length=32, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='company',
            name='insta',
            field=models.CharField(max_length=32, verbose_name='instagram'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=64, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=16, verbose_name='celular'),
        ),
        migrations.AlterField(
            model_name='company',
            name='youtube',
            field=models.CharField(max_length=70, verbose_name='youtube'),
        ),
    ]
