from django.urls import path
from .views import TaskCreateView, TaskUpdateView, task_list, task_detail, complete_task, delete_task, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', task_list, name='task_list'),
    path('<int:pk>/', task_detail, name='task_detail'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/complete/', complete_task, name='complete_task'),
    path('<int:pk>/delete/', delete_task, name='task_delete'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
