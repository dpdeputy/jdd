# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install uv
RUN pip install uv

# Install Godot 4.4.1
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://github.com/godotengine/godot-builds/releases/download/4.4.1-stable/Godot_v4.4.1-stable_linux.x86_64.zip -O /tmp/godot.zip && \
    unzip /tmp/godot.zip -d /tmp/ && \
    mv /tmp/Godot_v4.4.1-stable_linux.x86_64 /usr/local/bin/godot4 && \
    rm /tmp/godot.zip

# Copy pyproject.toml to leverage Docker cache
COPY pyproject.toml ./

# Install dependencies
RUN uv pip install .

# Copy the application source code
COPY src/ ./src/

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
