# Generated by Django 3.1.4 on 2021-02-02 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0044_auto_20210203_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerlike',
            name='likecus',
        ),
    ]
