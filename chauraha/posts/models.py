from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='posts')

    def __str__(self):
        return self.content[:15]

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body[:15]


class Subly(models.Model):
    body = models.TextField()
    comment = models.ForeignKey(Comment, on_delete= models.CASCADE, related_name= 'subly')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subly')

    def __str__(self):
        return self.body[:15]
