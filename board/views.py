from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Post
from .utils import Post_to_JSON

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'posts': list(map(Post_to_JSON, Post.objects.all())),
    }
    print(context)
    return render(request, "board.html", context)