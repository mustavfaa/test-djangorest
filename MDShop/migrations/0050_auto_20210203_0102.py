# Generated by Django 3.1.4 on 2021-02-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0049_customerlike_likecustomer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlike',
            name='like',
            field=models.ManyToManyField(null=True, to='MDShop.smartphone', verbose_name='Категория'),
        ),
    ]