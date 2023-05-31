from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import *
from .models import *

# Create your views here.


class BoardView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "board.html", self.get_context_data())

    def get_context_data(self, **kwargs):
        context = {
            'posts': Post.objects.all(),
        }
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = '/'


class UserListView(ListView):
    model = User
    paginate_by = 100


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/'


class PostListView(ListView):
    model = Post
    paginate_by = 100


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/'


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = '/'


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    success_url = '/'
