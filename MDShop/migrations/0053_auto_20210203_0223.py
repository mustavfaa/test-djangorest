# Generated by Django 3.1.4 on 2021-02-02 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0052_auto_20210203_0112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerlike',
            options={'ordering': ['-id']},
        ),
    ]
