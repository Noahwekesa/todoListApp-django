from django.contrib.admin.options import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods

from .models import Todo
from .forms import TodoForm


@login_required
def index(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    form = TodoForm()
    context = {
        'todos': todos, 'form': form
    }
    return render(request, 'index.html', context)


@login_required
@require_POST
def submit_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        messages.success(request, "To-do added Successfully")

        # return a htmx partial
        context = {
            'todo': todo
        }
        return render(request, 'index.html#todoitem-partial', context)


@login_required
@require_POST
def complete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = True
    todo.save()
    context = {
        'todo': todo
    }
    return render(request, 'index.html#todoitem-partial', context)


@login_required
@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    response = HttpResponse(status=204)
    response['HX-Trigger'] = 'delete-todo'
    return response
