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
from django.contrib.auth import views as auth_views
from django.urls import path

from board import views as board_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("board/", board_views.BoardView.as_view(), name="home"),
    path("board/post/create/", board_views.PostCreateView.as_view(), name="post/create"),
    path("board/post/list/", board_views.PostListView.as_view(), name="post/list"),
    path("board/post/<int:pk>/", board_views.PostDetailView.as_view(), name="post/get"),
    path("board/post/<int:pk>/update/", board_views.PostUpdateView.as_view(), name="post/update"),
    path("board/post/<int:pk>/delete/", board_views.PostDeleteView.as_view(), name="post/delete"),
    path("board/comment/create/", board_views.CommentCreateView.as_view(), name="comment/create"),
    path("board/comment/<int:pk>/update/", board_views.CommentUpdateView.as_view(), name="comment/update"),
    path("board/comment/<int:pk>/delete/", board_views.CommentDeleteView.as_view(), name="comment/delete"),
    path("board/reply/create/", board_views.ReplyCreateView.as_view(), name="reply/create"),
    path("board/reply/<int:pk>/update/", board_views.ReplyUpdateView.as_view(), name="reply/update"),
    path("board/reply/<int:pk>/delete/", board_views.ReplyDeleteView.as_view(), name="reply/delete"),
    path("board/user/create/", board_views.UserCreateView.as_view(), name="user/create"),
    path("board/user/list/", board_views.UserListView.as_view(), name="user/list"),
    path("board/user/login/", auth_views.LoginView.as_view(), name="user/login"),
    path("board/user/logout/", auth_views.LogoutView.as_view(), name="user/logout"),
]
