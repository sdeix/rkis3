from django.shortcuts import render
from django.views.generic import ListView,CreateView, DetailView
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CreateUserForm, CreatePostForm
from django.urls import reverse_lazy
from .models import Post, Comment



class SignUp(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('index')
    template_name = 'register/register.html'

class Login(LoginView):
    template_name = 'register/login.html'

class Logout(LogoutView):
    template_name = 'register/logout.html'


class Index(ListView):
    model = Post
    template_name = 'index.html'

class CreatePost(CreateView):
    form_class = CreatePostForm
    success_url = reverse_lazy('index')
    template_name = 'createpost.html'