from typing import Any, Dict

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Post, User
from .utils import Post_to_JSON

# Create your views here.


class BoardView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, "board.html", self.get_context_data())

    def get_context_data(self, **kwargs):
        context = {
            'posts': list(map(Post_to_JSON, Post.objects.all())),
        }
        return context


class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password']
    success_url = '/'


class UserListView(ListView):
    model = User
    paginate_by = 100


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        post: Post = kwargs['object']
        context = super().get_context_data(**kwargs)
        context['post'] = Post_to_JSON(post)
        return context
