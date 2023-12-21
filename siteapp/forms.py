from django.contrib.auth.forms import UserCreationForm
from .models import User, Post, Comment
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','name','avatar','desc')


class CreatePostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title','post_text','post_author')


class CreateCommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('com_text','com_author','com_post')



