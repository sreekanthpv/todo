from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    completed = models.BooleanField(default=False)
    task_name =models.CharField(max_length=30)

    def __str__(self):
        return self.task_name


