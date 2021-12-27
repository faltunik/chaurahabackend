from django.urls import path
from . import views
from .views import PostLikeAPI, AddLikeUnlikeView


urlpatterns = [
    path('post/', PostLikeAPI.as_view(), name="like_post"),
    path('postlike/', AddLikeUnlikeView.as_view(), name= "like_unlike_post")
]