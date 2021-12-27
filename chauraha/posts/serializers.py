from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models  import Post, Comment, Subly
from users.serializers import CustomUserSerializer

class PostSerializer(serializers.ModelSerializer):
    #userdetail = CustomUserSerializer(many=True, read_only = True)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='branch'
     )

    class Meta:
        model = Post
        fields = ('id', 'content', 'author',)

class PostLikeSerializer(serializers.ModelSerializer):
    # like = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='like'
    #  )
    class Meta:
        model = Post
        fields = ('id', 'like',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='branch'
     )
    class Meta:
        model = Comment
        fields = ('id', 'body', 'post', 'author',)


class SublySerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='branch'
     )
    class Meta:
        model = Subly
        fields = ('id', 'body', 'comment', 'author',)

        