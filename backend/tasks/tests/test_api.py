import pytest
from tasks.models import Task
from tasks.tests.factories import TaskFactory
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.fixture
def user(db):
    return get_user_model().objects.create_user(
        username="testuser",
        email="testuser@example.com",
        password="password123"
    )
@pytest.fixture
def api_client(db):
    client = APIClient()
    return client

@pytest.mark.django_db
def test_create_task(api_client, user):
    client = api_client
    client.force_authenticate(user=user)
    data = {"name": "New Task", "due_date": "2025-12-31T23:59:59Z"}
    response = client.post("/api/tasks/", data)
    assert response.status_code == 201
    assert Task.objects.filter(name="New Task").exists()

@pytest.mark.django_db
def test_list_tasks(api_client, user):
    client = api_client
    client.force_authenticate(user=user)
    TaskFactory.create_batch(10, owner=user)
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    assert len(response.json()["results"]) == 10
