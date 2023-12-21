from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('register',views.SignUp.as_view(),name='signup'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('createpost',views.CreatePost.as_view(),name='createpost'),
    path('updateprofile/<int:pk>/',views.UpdateProfile.as_view(),name='updateprofile'),
    path('detail/<int:pk>/',views.DetailPost.as_view(),name='detail'),
    path('createcomment/',views.CreateComment.as_view(),name='createcomment'),

    # path('post/<int:pk>',)
]