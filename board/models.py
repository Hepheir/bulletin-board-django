from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(null=False, max_length=16, unique=True)
    password = models.CharField(null=False, max_length=16)


class Post(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)


class Comment(models.Model):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
