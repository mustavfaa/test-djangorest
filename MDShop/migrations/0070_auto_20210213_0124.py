# Generated by Django 3.1.4 on 2021-02-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0069_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.PositiveSmallIntegerField(blank=True, verbose_name='цена'),
        ),
    ]
