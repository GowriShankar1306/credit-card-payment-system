# Credit Card Payment System

A backend-based Credit Card Payment System built using Django, FastAPI, MySQL, and Docker.

## Technologies

* Python
* Django & Django REST Framework
* FastAPI
* SQLAlchemy
* MySQL 8.0
* JWT Authentication
* Docker & Docker Compose
* Postman

## Project Structure

```text
credit_card_payment_system/
├── database/
├── django_backend/
├── fastapi_backend/
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Features

* User registration and login
* JWT authentication
* User profile management
* Credit card management
* Transaction management
* Payment processing
* Django Admin
* MySQL database
* Dockerized Django and FastAPI backends

## API

### Django

```text
http://localhost:8000
```

### FastAPI

```text
http://localhost:8001
```

Swagger documentation:

```text
http://localhost:8001/docs
```

## Docker

Start the application:

```bash
docker compose up -d
```

Check containers:

```bash
docker compose ps
```

Stop the application:

```bash
docker compose down
```

## Database

Database:

```text
credit_card_db
```

Database dump:

```text
database/credit_card_db.sql
```

## Security

* JWT authentication
* Password hashing
* Input validation
* No CVV storage
* Environment variables for credentials
* `.env` excluded from Git
* No real payment gateway integration

## Testing

APIs were tested using:

* Swagger UI
* Postman

Django Admin:

```text
http://localhost:8000/admin/
```
