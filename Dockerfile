FROM python:3.9-slim AS base

WORKDIR /app

# Install system dependencies + Docker CLI
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    ca-certificates \
    curl \
    gnupg \
    lsb-release && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*
FROM python:3.9-slim-buster

# Install necessary tools and utilities
RUN apt-get update && apt-get install -y \
    procps \
    curl \
    && rm -rf /var/lib/apt/lists/*

CMD ["python", "app.py"]



COPY requirements.txt .
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]



# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY . .

ENV DJANGO_SETTINGS_MODULE=myvoice.settings
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["gunicorn", "myvoice.wsgi:application", "--bind", "0.0.0.0:8000"]
