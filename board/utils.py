from .models import *


def User_to_JSON(user: User):
    return {
        'name': user.username,
    }


def Post_to_JSON(post: Post):
    return {
        'author': User_to_JSON(post.author),
        'content': post.content,
        'replies': Comment.objects.filter(post=post),
    }


def Comment_to_JSON(comment: Comment):
    return {
        'author': User_to_JSON(comment.author),
        'content': comment.content,
        'replies': Reply.objects.filter(comment=comment),
    }


def Reply_to_JSON(reply: Reply):
    return {
        'author': User_to_JSON(reply.author),
        'content': reply.content,
    }
