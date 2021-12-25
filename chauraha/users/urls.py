from django.urls import path
from . import views
from .views import MyTokenObtainPairView, CustomUserCreate

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('users/', CustomUserCreate.as_view(), name="create_user"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]