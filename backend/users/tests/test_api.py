import pytest
from rest_framework.test import APIClient
from users.tests.factories import UserFactory

@pytest.fixture
def api_client(db):
    client = APIClient()
    return client

@pytest.mark.django_db
def test_user_registration(api_client):
    data = {"username": "newuser", "password": "newpassword123"}
    response = api_client.post("/api/auth/register/", data)
    assert response.status_code == 201
    assert "id" in response.json()

@pytest.mark.django_db
def test_user_login(api_client):
    user = UserFactory(password="password123")
    data = {"username": user.username, "password": "password123"}
    response = api_client.post("/api/auth/login/", data)
    assert response.status_code == 200
    assert "access" in response.json()
