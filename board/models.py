from __future__ import annotations

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def get_by_natural_key(self, username: str | None):
        return super().get_by_natural_key(username)

    def create_superuser(self, username: str | None, password: str | None) -> User:
        user: User
        user = self.model(username=username)
        user.set_password(password)
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    username = models.CharField(null=False, max_length=16, unique=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self) -> bool:
        return self.is_admin

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


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
