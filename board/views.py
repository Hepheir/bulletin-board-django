from django.contrib import auth
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
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
    form_class = UserCreateForm
    success_url = '/'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)


class UserListView(ListView):
    model = User
    paginate_by = 100


class UserLoginView(View):
    template_name = 'board/user_login.html'
    form_class = UserLoginForm

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, self.get_context_data())

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            message = 'Login failed!, username password mismatch'
        else:
            message = form.errors
        return render(request, self.template_name, {**self.get_context_data(), 'message': message})

    def get_context_data(self, **kwargs):
        context = {
            'form': self.form_class()
        }
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = '/'


class PostListView(ListView):
    model = Post
    paginate_by = 100


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    success_url = '/'


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    success_url = '/'


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentUpdateForm
    success_url = '/'


class ReplyCreateView(CreateView):
    model = Reply
    form_class = ReplyCreateForm
    success_url = '/'


class ReplyUpdateView(UpdateView):
    model = Reply
    form_class = ReplyUpdateForm
    success_url = '/'