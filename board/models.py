from __future__ import annotations

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    title = models.CharField(null=False, max_length=80)
    content = models.CharField(null=False, max_length=1000)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    created_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    @property
    def comments(self):
        return Comment.objects.filter(post=self)

    def __str__(self) -> str:
        return f'{self.title} ({self.created_by})'


class Comment(models.Model):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    content = models.CharField(null=False, max_length=200)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    created_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    @property
    def replies(self):
        return Reply.objects.filter(comment=self)

    def __str__(self) -> str:
        return f'{self.content} ({self.created_by})'


class Reply(models.Model):
    comment = models.ForeignKey(Comment, null=False, on_delete=models.CASCADE)
    content = models.CharField(null=False, max_length=200)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    created_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
