# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=myvoice.settings
ENV PYTHONUNBUFFERED=1

# Expose the port for the application
EXPOSE 8000

# Run database migrations, collect static files, and start the server
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn myvoice.wsgi:application --bind 0.0.0.0:8000"]
