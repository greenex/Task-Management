from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    """
    owner = serializers.ReadOnlyField(source="owner.username")  # Read-only owner field

    class Meta:
        model = Task
        fields = ["id", "name", "description", "due_date", "completed", "owner"]
