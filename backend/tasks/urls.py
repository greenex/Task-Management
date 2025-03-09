from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Create a router and register TaskViewSet
router = DefaultRouter()
router.register(r"", TaskViewSet, basename="tasks")

# Include router URLs
urlpatterns = [
    path("", include(router.urls)),  # Auto-generates all CRUD routes
]
