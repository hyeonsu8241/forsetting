from django.contrib.auth.models import User
from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=10, null=True, default="untitled")
    content = models.TextField()

    created_at = models.DateField(auto_now=True)