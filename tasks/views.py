from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Task

# Vista para listar tareas
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Vista para detalle de tarea
@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Obtiene la tarea del usuario autenticado
    return render(request, 'tasks/task_detail.html', {'task': task})

# Vista para crear tarea
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description']
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Asigna la tarea al usuario autenticado
        return super().form_valid(form)

# Vista para actualizar tarea
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = '/tasks/'

    def get_queryset(self):
        # Asegura que solo se puedan actualizar tareas del usuario autenticado
        return Task.objects.filter(user=self.request.user)

# Vista para marcar tarea como completada
@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Obtiene la tarea del usuario autenticado
    task.completed = True
    task.save()
    return redirect('task_list')

# Vista para eliminar tarea
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Asegura que el usuario solo acceda a sus tareas
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# Vista para registro de usuarios
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})
