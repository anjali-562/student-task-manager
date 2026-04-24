from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST

from .forms import TaskForm
from .models import Task

def _add_bootstrap_classes(form):
    for field in form.fields.values():
        existing_class = field.widget.attrs.get('class', '')
        field.widget.attrs['class'] = (f'{existing_class} form-control').strip()
    return form


@require_http_methods(['GET', 'POST'])
def register_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()

    context = {'form': _add_bootstrap_classes(form)}
    return render(request, 'tasks/register.html', context)


@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('task_list')
    else:
        form = AuthenticationForm(request)

    context = {'form': _add_bootstrap_classes(form)}
    return render(request, 'tasks/login.html', context)


@login_required
@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()
    context = {
        'tasks': tasks,
        'form': form,
        'total_tasks': tasks.count(),
    }
    return render(request, 'tasks/task_list.html', context)


@login_required
@require_POST
def add_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('task_list')

    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
        'form': form,
        'total_tasks': tasks.count(),
    }
    return render(request, 'tasks/task_list.html', context)


@login_required
@require_POST
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save(update_fields=['completed'])
    return redirect('task_list')


@login_required
@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')


@login_required
@require_http_methods(['GET', 'POST'])
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    context = {'form': form, 'task': task}
    return render(request, 'tasks/edit_task.html', context)
