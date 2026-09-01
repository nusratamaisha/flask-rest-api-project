# Flask Docker REST API

A small REST API (Store / Item / Tag / User) for practicing Flask, Docker,
and deployment. Originally built while following the "REST APIs with Flask
and Python" course.

## Stack

- Flask + Flask-Smorest (OpenAPI-documented blueprints)
- SQLAlchemy + Flask-Migrate (Alembic migrations)
- Flask-JWT-Extended (access tokens, revocation blocklist)
- RQ + Redis (background email job on registration)
- Gunicorn (production WSGI server)
- Docker / docker-compose for local dev
- Postgres (Neon in production)
- Deployed on Render
- Manually tested with Insomnia

## Running locally

```
docker compose up --build
```

## Endpoints

See the Swagger UI at `/swagger-ui` once the app is running for the full,
auto-generated endpoint reference.
