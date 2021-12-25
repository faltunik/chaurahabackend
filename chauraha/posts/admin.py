from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class CustomUserAdmin(admin.ModelAdmin):
  list_display = ['author', 'id', ]


# register comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['id', 'author']




