# Generated by Django 3.1.4 on 2021-02-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0072_remove_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='цена'),
        ),
    ]