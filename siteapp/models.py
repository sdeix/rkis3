from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, FileExtensionValidator
from django.forms import forms
from django.urls import reverse

class User(AbstractUser):
    name = models.CharField("имя",max_length=20,blank=True, validators=[RegexValidator(regex='^[а-яА-Я-]*$',message='только ририллица и дефис', code='invalid_username')])
    def validate_image(value):
        size_limit = 2*1024*1024
        if value.size > size_limit:
            raise forms.ValidationError("размер файла не должен превышать 2Mb")
    avatar = models.FileField("аватар",upload_to='avatars/',blank=True,validators=[validate_image,FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])])
    desc = models.TextField("описание",max_length=300,blank=True)
    # def get_info(self):
    #     return reverse('bio',args=[srt(self.id)])
    class Meta(AbstractUser.Meta):
        pass

class Post(models.Model):
    title = models.CharField('заголовок поста',max_length=30)
    post_text = models.TextField('текст поста',max_length=300)
    post_author = models.ForeignKey(User,verbose_name='автор поста', on_delete=models.CASCADE)

    def comments(self):
        comms = Comment.objects.filter(com_post=self)
        return comms

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    com_text = models.TextField('текст комментария',max_length=200)
    com_author = models.ForeignKey('User',verbose_name='автор комментария', on_delete=models.CASCADE)
    com_post = models.ForeignKey('Post',verbose_name="пост", on_delete=models.CASCADE)
    def __str__(self):
        return self.com_author
