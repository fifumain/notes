build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d 

down:
	docker compose down

show-logs:
	docker compose logs

show-logs-api:
	docker compose logs api

makemigrations:
	docker compose run --rm api python manage.py makemigrations

migrate:
	docker compose run --rm api python manage.py migrate

collectstatic:
	docker compose run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker compose run --rm api python manage.py createsuperuser

down-v:
	docker compose down -v


authors-db:
	docker composeexec postgres psql --username=postgres --dbname=notes_db

flake8:
	docker compose exec api flake8 .

black-check:
	docker compose exec api black --check --exclude=migrations .

black-diff:
	docker compose exec api black --diff --exclude=migrations .

black:
	docker compose exec api black --exclude=migrations .

isort-check:
	docker compose exec api isort . --check-only --skip venv --skip migrations

isort-diff:
	docker compose exec api isort . --diff --skip venv --skip migrations

isort:
	docker compose exec api isort . --skip venv --skip migrations