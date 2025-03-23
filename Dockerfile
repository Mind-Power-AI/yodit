# Use a Python base image
FROM python:3.9-slim AS base

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=myvoice.settings
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8000

# Define command to run the app
CMD ["gunicorn", "myvoice.wsgi:application", "--bind", "0.0.0.0:8000"]
