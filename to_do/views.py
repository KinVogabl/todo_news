from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
import django.views.generic

from to_do.forms import MyUserCreationForm
from to_do.models import Task


class UserRegistrationView(django.views.generic.FormView):
    template_name = 'register.html'
    form_class = MyUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super(UserRegistrationView, self).get(*args, **kwargs)


class TaskView(LoginRequiredMixin, django.views.generic.ListView):
    model = Task
    template_name = 'todo.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class UpdateTaskView(LoginRequiredMixin, django.views.generic.UpdateView):
    model = Task
    fields = ['text']
    template_name = 'update_todo.html'
    success_url = '/'


class DeleteTaskView(LoginRequiredMixin, django.views.generic.DeleteView):
    model = Task
    template_name = 'delete_todo.html'
    success_url = "/"


class CreateTaskView(LoginRequiredMixin, django.views.generic.CreateView):
    model = Task
    fields = ['text']
    template_name = 'update_todo.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

