# Generated by Django 3.2.4 on 2023-02-23 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='limitedtimeoffer',
            options={'verbose_name': 'promoção', 'verbose_name_plural': 'promoções'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'produto', 'verbose_name_plural': 'produtos'},
        ),
    ]
