# Generated by Django 3.1.4 on 2021-02-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0042_auto_20210202_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='likecus',
            field=models.ManyToManyField(to='MDShop.smartphone', verbose_name='лайк'),
        ),
    ]
