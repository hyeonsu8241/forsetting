from django.contrib.auth.models import User
from django.db import models


# class TodoList(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=False)
#     title = models.CharField(max_length=20, null=True, default="todo list")
#
#     def __str__(self):
#         return self.title


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo', null=True)
    content = models.CharField(max_length=50, null=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.content