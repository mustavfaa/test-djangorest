# Generated by Django 3.1.4 on 2021-02-07 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0057_auto_20210207_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerlike',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='customerlike',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
