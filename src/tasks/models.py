from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    description = models.CharField(max_length=200)
    is_completed = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description}'
