# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install uv
RUN pip install uv

# Copy pyproject.toml to leverage Docker cache
COPY pyproject.toml ./

# Install all dependencies, including for tests and docs
RUN uv pip install -e ".[test,docs]" --system

# Copy the application source code
COPY . .

# Define the command to run the ADK agent
CMD ["python", "-m", "src.adk_agent.main"]