# Django Task Manager API

This is a sample project that provides a basic task management system with user authentication and task CRUD operations.

---

## Features

- **User Authentication**: 
  - Register users
  - Login and obtain JSON Web Tokens (JWT)
  - Refresh tokens for continuous authentication
  
- **Task Management**:
  - Create, read, update, and delete tasks
  - Filter tasks by completion status
  - Sort tasks by due date or name
  - Search tasks by name or description
  - Ensure each user can only manage their own tasks

- **Celery Integration**:
  - Schedule task reminders
  - Clean up old completed tasks

---

## Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/greenex/Task-Management.git
    cd Task-Management
    ```

2. **create .env file**:
    ```bash
    cp .env.example .env
    ```

3. **Start Docker Services**:
    ```bash
    docker-compose up -d
    ```

4. **Access the Application**:
    - **API Root**: `http://127.0.0.1:8000/api/`
    - **Admin Panel**: `http://127.0.0.1:8000/admin/`

---

## Running Tests

To run the test suite:
```bash
docker-compose exec backend pytest
```

## Environment Variables
```bash
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```


---

## API Endpoints

**Authentication**
- **POST** `/api/auth/register/`: Register a new user
- **POST** `/api/auth/login/`: Obtain JWT
- **POST** `/api/auth/refresh/`: Refresh JWT

**Tasks**
- **GET** `/api/tasks/`: List all tasks (for the authenticated user)
- **POST** `/api/tasks/`: Create a new task
- **GET** `/api/tasks/<id>/`: Retrieve a single task
- **PUT** `/api/tasks/<id>/`: Update a task
- **DELETE** `/api/tasks/<id>/`: Delete a task

---

## Directory Structure

```bash
backend/
├── project/
│   ├── settings.py
│   ├── urls.py
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tasks.py
│   ├── urls.py
├── users/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
.env.example
docker-compose.yml
Dockerfile
requirements.txt
pytest.ini
README.md
```
