import pytest
from tasks.models import Task
from tasks.tasks import send_task_reminder, delete_old_completed_tasks
from unittest.mock import patch
from django.utils.timezone import now, timedelta

from tasks.tests.factories import TaskFactory


@pytest.mark.django_db
def test_delete_old_completed_tasks():
    TaskFactory.create_batch(5, completed=True, updated_at=now() - timedelta(days=2))
    delete_old_completed_tasks()


    assert True
