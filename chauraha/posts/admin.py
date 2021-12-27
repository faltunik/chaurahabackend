from django.contrib import admin
from .models import Post, Comment, Subly

# Register your models here.
@admin.register(Post)
class CustomUserAdmin(admin.ModelAdmin):
  list_display = ['author', 'id', 'content', ]


# register comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['id', 'author']

@admin.register(Subly)
class SublyAdmin(admin.ModelAdmin):
  list_display = ['id', 'author']



