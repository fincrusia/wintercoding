# Generated by Django 2.1 on 2018-10-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20181029_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due',
            field=models.DateTimeField(verbose_name='date'),
        ),
    ]
