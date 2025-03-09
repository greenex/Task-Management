from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to create, update, delete, and retrieve tasks.
    Supports filtering, sorting, and pagination.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Enable filtering & sorting
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    # Define filters
    filterset_fields = ["completed"]  # Allows ?completed=true or ?completed=false
    ordering_fields = ["due_date", "name"]  # Allows ?ordering=-due_date
    search_fields = ["name", "description"]  # Allows ?search=keyword

    def get_queryset(self):
        return self.request.user.tasks.all()  # Users only see their own tasks

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_object(self):
        """Ensure users can only modify their own tasks."""
        obj = super().get_object()
        if obj.owner != self.request.user:
            raise PermissionDenied("You do not have permission to modify this tasks.")
        return obj
