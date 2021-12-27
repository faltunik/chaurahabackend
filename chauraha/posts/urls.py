from django.urls import path
from . import views
from .views import PostLikeAPI


urlpatterns = [
    path('post/', PostLikeAPI.as_view(), name="like_post"),
]