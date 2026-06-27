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
