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

test:
	docker compose run --rm api pytest -p no:warnings --cov=. --cov-report html