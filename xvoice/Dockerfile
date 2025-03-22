FROM python:3.9-slim AS base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=myvoice.settings
ENV PYTHONUNBUFFERED=1
FROM ubuntu:20.04

# Install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python

# Set up your application
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# Use python3 or the symlinked python
CMD ["python", "python3.py"]


EXPOSE 8000

CMD ["gunicorn", "myvoice.wsgi:application", "--bind", "0.0.0.0:8000"]
