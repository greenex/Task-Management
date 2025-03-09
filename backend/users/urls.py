from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),  # User Registration
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # JWT Login
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Refresh JWT Token
]
