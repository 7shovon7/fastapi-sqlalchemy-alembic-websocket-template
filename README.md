# Simplest Starter Kit for FastAPI, SQLAlchemy, Alembic and WebSocket

Overcomplicating and overengineering is really really bad! At the same time we need all the important elements for future expansion. Here comes this FastAPI boilerplate template.

This is as simple as any beginner can start with. At the same time it includes most of the important elements to be the easiest starting point for a strong FastAPI API project.

To start with it:

- Create a new project

```bash
mkdir project-name
cd project-name
```

- Clone the repo

```bash
git clone https://github.com/7shovon7/fastapi-sqlalchemy-alembic-websocket-template.git .
```

- Create virtual environment (Consider choosing the right one - python or python3 and pip or pip3)

```bash
python3 -m venv venv
source venv/bin/activate
```

- Install the dependencies

```bash
pip3 install -r requirements.txt
```

## App settings

- Add `.env` file and update.
- Update settings data in `api/config.py`.

## Database

- Change the `DATABASE_URI` value accordingly in `.env` file.
- If database type is not SQLite3, remove `connect_args` inside `api/database/__init__.py` file.
- Put all the database table models (sqlalchemy models) inside `api/database/models.py` file. As the `Base` variable of `migrations/env.py` should come from the database tables file, so this is better for small or mid sized project.
- Setup schemas independently inside public folders under each modules/apps.

## DB Creation and Migration

Create migration

```bash
alembic revision --autogenerate -m 'Initial migration'
```

Apply migration

```bash
alembic upgrade head
```

## Run api

```bash
python3 asgi.py
```

## Please consider deleting any migration files unintentionally pushed to `migrations/versions/` directory
