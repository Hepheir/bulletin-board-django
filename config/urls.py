"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from board import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: redirect('board/', permanent=True)),
    path("board/", views.BoardView.as_view(), name="home"),
    path("board/post/create/", views.PostCreateView.as_view(), name="post/create"),
    path("board/post/list/", views.PostListView.as_view(), name="post/list"),
    path("board/post/<int:pk>/", views.PostDetailView.as_view(), name="post/get"),
    path("board/post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post/update"),
    path("board/comment/create/", views.CommentCreateView.as_view(), name="comment/create"),
    path("board/comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment/update"),
    path("board/reply/create/", views.ReplyCreateView.as_view(), name="reply/create"),
    path("board/reply/<int:pk>/update/", views.ReplyUpdateView.as_view(), name="reply/update"),
    path("board/user/create/", views.UserCreateView.as_view(), name="user/create"),
    path("board/user/list/", views.UserListView.as_view(), name="user/list"),
    path("board/user/login/", views.UserLoginView.as_view(), name="user/login"),
]
