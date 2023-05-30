from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(null=False, max_length=16, unique=True)
    password = models.CharField(null=False, max_length=16)
    created_at = models.DateTimeField(null=False, auto_now_add=True)


class Post(models.Model):
    title = models.CharField(null=False, max_length=80)
    content = models.CharField(null=False, max_length=1000)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    created_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    content = models.CharField(null=False, max_length=200)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    created_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, null=False, on_delete=models.CASCADE)
    content = models.CharField(null=False, max_length=200)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    created_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
