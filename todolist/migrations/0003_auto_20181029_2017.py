# Generated by Django 2.1 on 2018-10-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todo_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='content',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(default='', max_length=1000),
        ),
    ]