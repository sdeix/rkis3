from django.shortcuts import render
from django.views.generic import ListView,CreateView, DetailView,UpdateView, DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CreateUserForm, CreatePostForm, CreateCommentForm
from django.urls import reverse_lazy
from .models import Post, Comment, User
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

class SignUp(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('index')
    template_name = 'register/register.html'

class Login(LoginView):
    template_name = 'register/login.html'

class Logout(LogoutView):
    template_name = 'register/logout.html'

class UpdateProfile(UpdateView):
    model = User
    success_url = reverse_lazy('index')
    template_name = 'register/update.html'
    fields = ['name','avatar','desc']


class Index(ListView):
    model = Post
    paginate_by = 4
    template_name = 'index.html'

class CreatePost(CreateView):
    form_class = CreatePostForm
    success_url = reverse_lazy('index')
    template_name = 'createpost.html'


class DetailPost(DetailView):
    model = Post
    template_name = 'detail.html'
    


class CreateComment(CreateView):
    
    form_class = CreateCommentForm
    success_url = reverse_lazy('index')
    template_name = "createcomment.html"


class UpdateComment(UpdateView):
    model = Comment
    success_url = reverse_lazy('index')
    template_name = 'updatecomment.html'
    fields = ['com_text','com_img']

class DeleteComment(DeleteView):
    model = Comment
    success_url = reverse_lazy('index')
    template_name = 'deletecomment.html'