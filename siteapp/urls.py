from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('register',views.SignUp.as_view(),name='signup'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('createpost',views.CreatePost.as_view(),name='createpost'),

    # path('post/<int:pk>',)
]