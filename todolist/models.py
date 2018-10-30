from django.db import models

# Create your models here.

class Todo(models.Model):
    due = models.DateTimeField("date")
    done = models.BooleanField(default = False)
    title = models.CharField(max_length = 1000, default = '')
    content = models.CharField(max_length = 1000, default = '')
    priority = models.IntegerField(default = 0)