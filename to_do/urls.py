from to_do.views import TaskView, UpdateTaskView, DeleteTaskView, CreateTaskView, UserRegistrationView
from django.urls import path

urlpatterns = [
    path('accounts/registration', UserRegistrationView.as_view(), name='register'),



    path('', TaskView.as_view()),
    path('todo/update_todo/<int:pk>', UpdateTaskView.as_view(), name='update'),
    path('todo/delete_todo/<int:pk>', DeleteTaskView.as_view(), name='delete'),
    path('todo/create_todo', CreateTaskView.as_view(), name='create')
]