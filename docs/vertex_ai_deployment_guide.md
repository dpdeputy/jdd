# Vertex AI Deployment Guide

This guide provides step-by-step instructions for deploying the ADK-based agent to the Vertex AI Agent Engine on Google Cloud Platform (GCP).

## Prerequisites

Before you begin, ensure you have the following:

1.  **A Google Cloud Project:** You need a GCP project with billing enabled.
2.  **Required APIs Enabled:** In your GCP project, enable the following APIs:
    *   Artifact Registry API (`artifactregistry.googleapis.com`)
    *   Vertex AI API (`aiplatform.googleapis.com`)
    *   Cloud Build API (`cloudbuild.googleapis.com`)
3.  **Permissions:** You need the following IAM roles for your user account or a service account:
    *   `roles/artifactregistry.writer` (to push container images)
    *   `roles/aiplatform.admin` (to manage Vertex AI resources)
    *   `roles/cloudbuild.builds.editor` (to run builds)
    *   `roles/storage.admin` (for the agent to access GCS buckets)
4.  **Google Cloud CLI:** Make sure you have the [gcloud CLI installed and configured](https://cloud.google.com/sdk/docs/install).

## Deployment Steps

The deployment process involves three main stages: building the container image, pushing it to the Artifact Registry, and deploying it to the Vertex AI Agent Engine.

### 1. Set Up Your Environment

First, set up some environment variables in your shell to make the following commands easier.

```bash
export PROJECT_ID="your-gcp-project-id"
export REGION="your-gcp-region" # e.g., us-central1
export REPO_NAME="ai-agents-repo"
export IMAGE_NAME="gcs-listing-agent"
export IMAGE_TAG="latest"

gcloud config set project $PROJECT_ID
gcloud config set compute/region $REGION
```
Replace `your-gcp-project-id` and `your-gcp-region` with your actual project ID and desired region.

### 2. Create an Artifact Registry Repository

You need a repository in the Artifact Registry to store your container images.

```bash
gcloud artifacts repositories create $REPO_NAME \
    --repository-format=docker \
    --location=$REGION \
    --description="Repository for AI agent container images"
```

### 3. Build and Push the Container Image

Now, use Cloud Build to build the Docker image and push it to the repository you just created. This command runs the build process entirely on GCP.

```bash
gcloud builds submit --tag ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG} .
```

This command will use the `Dockerfile` in the current directory, build the image, and tag it appropriately for the Artifact Registry.

### 4. Deploy to Vertex AI Agent Engine

With the container image in the Artifact Registry, you can now deploy it as a "Reasoning Engine" (the API name for an Agent Engine instance) on Vertex AI.

**Note:** The Vertex AI Agent Engine is a new and evolving product. The exact deployment method (e.g., using a YAML file, `gcloud` commands, or the Cloud Console) should be verified with the latest [official Google Cloud documentation](https://cloud.google.com/vertex-ai/docs/agent-engine/overview).

You would typically perform this step through the Google Cloud Console by navigating to the Vertex AI section and finding the Agent Engine or Reasoning Engines page. From there, you can create a new Reasoning Engine and point it to the container image you pushed to the Artifact Registry.

## Running the Deployed Agent

Once deployed, the agent can be invoked via the Vertex AI API. You would use a client library (like the `google-cloud-aiplatform` Python library) to get a reference to the deployed reasoning engine and then call its `run` or `execute` method with a prompt.

Example Python code snippet (for illustration):

```python
from google.cloud import aiplatform

# Initialize the client
aiplatform.init(project="your-gcp-project-id", location="your-gcp-region")

# Get a reference to the deployed agent
# The name will be based on what you configured in the Cloud Console.
agent_engine = aiplatform.ReasoningEngine("your-deployed-agent-engine-name")

# Run the agent
response = agent_engine.run(
    prompt="Please list all of the Google Cloud Storage buckets in the project."
)

print(response)
```

This guide provides a high-level overview. Always refer to the official Google Cloud documentation for the most up-to-date and detailed instructions.