from django.db import models
from django.db.models import QuerySet
from django.contrib.auth.models import User

class TodoTime(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 


class CompletedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=True)

class PendingManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=False)

class _Todo(TodoTime):
    title = models.CharField(max_length=120)
    memo = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        abstract = True

class TodoForm(_Todo):
    pass

class Todo(_Todo): 
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todo"
    )
    

    object = models.Manager()
    completed = CompletedManager()
    pending = PendingManager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title