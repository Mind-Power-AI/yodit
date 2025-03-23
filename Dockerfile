FROM python:3.9-slim-buster

# Set working directory
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*
# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Define entry point for your app
CMD ["python", "app.py"]


FROM debian:buster

# Install necessary packages for adding Docker repository


# Add Docker's official GPG key
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Set up Docker repository
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(grep -oP 'VERSION_CODENAME=\K\w+' /etc/os-release) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package index and install Docker CLI
RUN apt-get update && apt-get install -y docker-ce-cli docker-ce containerd.io && rm -rf /var/lib/apt/lists/*



CMD ["bash"]

