# Stage 1: Base image with common dependencies
FROM python:3.11-slim AS base

# Install uv and Godot
RUN pip install uv
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://github.com/godotengine/godot-builds/releases/download/4.4.1-stable/Godot_v4.4.1-stable_linux.x86_64.zip -O /tmp/godot.zip && \
    unzip /tmp/godot.zip -d /tmp/ && \
    mv /tmp/Godot_v4.4.1-stable_linux.x86_64 /usr/local/bin/godot4 && \
    rm /tmp/godot.zip

WORKDIR /app


# Stage 2: Development image
FROM base AS dev

# Copy project files
COPY . .

# Create virtual environment and install all dependencies in editable mode
RUN uv venv && \
    . .venv/bin/activate && \
    uv pip install -e ".[test,docs]"

# Set the default command to a shell
CMD ["/bin/bash"]


# Stage 3: Production image
FROM base AS prod

# Copy pyproject.toml to leverage Docker cache
COPY pyproject.toml ./

# Install only production dependencies
RUN uv pip install . --system

# Copy the application source code
COPY src/ ./src/

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
