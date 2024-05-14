# Simplest Starter Kit for FastAPI, SQLAlchemy, Alembic and WebSocket

To start with it -

```bash
mkdir project-name
cd project-name
git clone https://github.com/7shovon7/fastapi-sqlalchemy-alembic-websocket-template.git .
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## App settings

- Add `.env` file and update.
- Update settings data in `app/config.py`.

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
