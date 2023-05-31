from django import forms

from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_by']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'content', 'created_by']
