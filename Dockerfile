# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install uv
RUN pip install uv

# Copy pyproject.toml to leverage Docker cache
COPY pyproject.toml ./

# Install dependencies
RUN uv pip install . --system

# Copy the application source code
COPY src/ ./src/

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
