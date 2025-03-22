FROM python:3.9-slim as base

WORKDIR /app
RUN ls -la /app

# Copy only requirements first
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

CMD ["gunicorn", "myvoice.wsgi:application", "--bind", "0.0.0.0:8000"]
