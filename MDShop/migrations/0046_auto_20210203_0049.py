# Generated by Django 3.1.4 on 2021-02-02 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0045_remove_customerlike_likecus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='likeCustomer',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='likecus',
        ),
        migrations.DeleteModel(
            name='like',
        ),
    ]