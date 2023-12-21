from django.shortcuts import render
from django.views.generic import ListView,CreateView, DetailView
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CreateUserForm
from django.urls import reverse_lazy

def index(request):
    return render(request,'index.html')


class SignUp(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('index')
    template_name = 'register/register.html'

class Login(LoginView):
    template_name = 'register/login.html'

class Logout(LogoutView):
    template_name = 'register/logout.html'
