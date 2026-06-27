# Task Project

This project can be run entirely with Docker.

## Prerequisites

- Docker
- Docker Compose

## Environment variables

Create a file named `.env` in the project root with the following content:

```env
SECRET_KEY=django-insecure-y_=ppx4ybw#07bphpll%oya!6zxl5jx+@3_=9ocq@g0^3c3rku
DEBUG=True
DB_NAME=task_db
DB_USER=user
DB_PASSWORD=20022020Ab
DB_HOST=db
DB_PORT=5432
```

## Run with Docker

Build and start the containers:

```bash
docker compose up --build
```

The application will be available at:

```text
http://localhost:8000
```

## API endpoints

Base URL:

```text
http://localhost:8000
```

### Authentication

- POST /api/users/register/ — register a new user
- POST /api/users/login/ — login and get JWT tokens
- POST /api/users/logout/ — logout the authenticated user
- POST /api/users/token/refresh/ — refresh the JWT access token

### Tasks

- GET /api/tasks/ — list all tasks
- POST /api/tasks/ — create a new task
- GET /api/tasks/{id}/ — get one task by ID
- PUT /api/tasks/{id}/ — update a task
- DELETE /api/tasks/{id}/ — delete a task
- PATCH /api/tasks/{id}/update-status/ — update task status

### Employees

- GET /api/employees/ — list all employees
- POST /api/employees/ — create a new employee
- GET /api/employees/{id}/ — get one employee by ID
- PUT /api/employees/{id}/ — update an employee
- DELETE /api/employees/{id}/ — delete an employee

### Admin

- GET /admin/ — Django admin panel

> Most API endpoints require authentication. Use the JWT token received from login as a Bearer token in the Authorization header.

## Useful commands

Stop the containers:

```bash
docker compose down
```

View logs:

```bash
docker compose logs -f
```

Rebuild without cache:

```bash
docker compose build --no-cache
```
