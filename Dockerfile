# Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements (optional if you're using a requirements file)
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install torch torchvision transformers pillow

# Copy the application code
COPY . .

# Run the app when the container starts
CMD ["python", "app.py"]
