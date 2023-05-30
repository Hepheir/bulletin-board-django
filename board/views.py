from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import View

from .models import Post
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
