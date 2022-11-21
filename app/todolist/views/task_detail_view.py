from django.shortcuts import get_object_or_404
from todolist.models import Tasks
from django.views.generic import DetailView


class TaskDetailView(DetailView):
    template_name = 'task.html'
    model = Tasks
    context_object_name = 'todo_task'