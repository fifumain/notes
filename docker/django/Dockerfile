# Указываем версию Python, используемую в проекте
ARG PYTHON_VERSION=3.11.2-bullseye

FROM python:${PYTHON_VERSION} as python

# Устанавливаем системные зависимости для сборки и работы с PostgreSQL
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Задаем рабочую директорию
WORKDIR /app

# Устанавливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта
COPY . .

# Настраиваем файлы entrypoint и start
COPY ./docker/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && chmod +x /entrypoint

COPY ./docker/django/start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start

# Указываем команду по умолчанию
ENTRYPOINT ["/entrypoint"]
