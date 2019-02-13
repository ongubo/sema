from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)


class Comments(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
