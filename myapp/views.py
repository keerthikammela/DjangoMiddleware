import os
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import User
from .forms import UserForm, CustomUserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'myapp/user_list.html'
    context_object_name = 'users'  


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'myapp/user_form.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'myapp/user_form.html'
    success_url = reverse_lazy('user_list')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'myapp/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'myapp/user_detail.html'
    context_object_name = 'user'

class LogoutConfirmView(LoginRequiredMixin, TemplateView):
    template_name = "myapp/registration/logout_confirm.html"

class LogoutSubmitView(LoginRequiredMixin, LogoutView):
    pass

class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "myapp/registration/register.html"
    success_url = reverse_lazy("login")


LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), '../request_logs.log')

class LogListView(LoginRequiredMixin, TemplateView):
    template_name = "myapp/logs.html"

    def get_context_data(self, **kwargs):
        """Read the log file and pass logs to the template."""
        context = super().get_context_data(**kwargs)
        try:
            with open(LOG_FILE_PATH, 'r') as f:
                context['logs'] = f.readlines()
        except FileNotFoundError:
            context['logs'] = ["No logs found."]
        return context

