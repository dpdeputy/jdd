# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install uv
RUN pip install uv

# Install gcloud CLI
RUN apt-get update && apt-get install -y curl
RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz
RUN mkdir -p /usr/local/gcloud \
    && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
    && /usr/local/gcloud/google-cloud-sdk/install.sh
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

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
