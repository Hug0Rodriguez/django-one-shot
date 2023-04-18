from django.db import models


# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)


class TodoItem(models.Model):
    task = models.CharField(max_length=100)
    due_date = models.DateField(
        null=True,
        blank=True,
    )
    is_completed = models.BooleanField(default=False)
    list = models.ForeignKey(
        "Todolist",
        related_name="items",
        on_delete=models.CASCADE,
    )
