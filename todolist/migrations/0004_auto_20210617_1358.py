# Generated by Django 2.2.19 on 2021-06-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20210617_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
    ]
