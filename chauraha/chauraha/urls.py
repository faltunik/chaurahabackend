"""chauraha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts import views
from rest_framework.routers import DefaultRouter



post_router = DefaultRouter()
comment_router = DefaultRouter()
subly_router = DefaultRouter()
# register our viewset with router
post_router.register('post', views.PostView, basename = 'post')
comment_router.register('comment', views.CommentView, basename= 'comments')
subly_router.register('subly', views.SublyView, basename= 'sublys')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('like/', include('posts.urls')),
    path('post/', include(post_router.urls)),
    path('comments/', include(comment_router.urls)),
    path('sublys/', include(subly_router.urls)),
]
