# Dockerfile for taifa_insights
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential default-libmysqlclient-dev libssl-dev libffi-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Collect static files in production
RUN mkdir -p /vol/web/static /vol/web/media

EXPOSE 8000

CMD ["gunicorn", "taifa_insights.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
