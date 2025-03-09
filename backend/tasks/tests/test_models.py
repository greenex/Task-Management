import pytest
from tasks.models import Task
from django.utils.timezone import now, timedelta

from users.tests.factories import UserFactory


@pytest.mark.django_db
def test_task_str():
    user = UserFactory()
    task = Task.objects.create(name="Test Task", owner=user, due_date=now() + timedelta(days=1))
    assert str(task) == "Test Task"

@pytest.mark.django_db
def test_task_fields():
    user = UserFactory()
    task = Task.objects.create(
        name="Test Task",
        description="This is a test task.",
        owner=user,
        due_date=now() + timedelta(days=1),
        completed=True,
    )
    assert task.name == "Test Task"
    assert task.description == "This is a test task."
    assert task.completed is True
    assert task.due_date > now()
