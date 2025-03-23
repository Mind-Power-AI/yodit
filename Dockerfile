FROM python:3.9-slim AS base

WORKDIR /app

# Install system dependencies

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]

COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

COPY . .

ENV DJANGO_SETTINGS_MODULE=myvoice.settings
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["gunicorn", "myvoice.wsgi:application", "--bind", "0.0.0.0:8000"]
