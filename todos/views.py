from django.shortcuts import render
from .models import TodoList


# Create your views here.
def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        "todo_lists": todo_lists,
    }
    return render(request, "todos/todo_lists.html", context)
