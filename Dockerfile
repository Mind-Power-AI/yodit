FROM python:3.9-slim-buster

# Install necessary system utilities
RUN apt-get update && apt-get install -y \
    procps \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app
RUN apt-get update && apt-get install -y docker-ce-cli && rm -rf /var/lib/apt/lists/*

apt-get install -y \
    ca-certificates \
    gnupg \
    lsb-release

apt-get install -y docker-ce-cli docker-ce containerd.io


# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Define entry point for your app
CMD ["python", "app.py"]
