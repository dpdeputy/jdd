# Deployment Guide: ADR Service on Google Cloud

This guide provides step-by-step instructions for deploying the ADR (Architectural Decision Records) service to Google Cloud Run and integrating it with Google AgentSpace.

This approach uses Google Cloud Run as a simple, serverless deployment target, which is a great first step before moving to a more complex setup like the Vertex AI Agent Engine.

## Prerequisites

Before you begin, ensure you have the following:
1.  **A Google Cloud Project:** With billing enabled.
2.  **Google Cloud SDK (`gcloud`):** [Installed and authenticated](https://cloud.google.com/sdk/docs/install).
3.  **Docker:** [Installed and running](https://docs.docker.com/get-docker/) on your local machine.
4.  **Enabled APIs:** In your GCP project, enable the **Artifact Registry API** and the **Cloud Run API**.
5.  **Permissions:** You need IAM roles like `roles/run.admin` and `roles/artifactregistry.writer` in your project.

---

## Step 1: Build the Docker Image

First, build the Docker image for the application. This command packages the FastAPI application into a container.

From the root of the repository, run:
```bash
docker build -t adr-service:latest .
```

---

## Step 2: Push the Image to Google Artifact Registry

Next, you need to store your container image in Google Artifact Registry, a private container registry on GCP.

1.  **Create an Artifact Registry Repository:**
    Choose a location (e.g., `us-central1`) and create a Docker repository.
    ```bash
    gcloud artifacts repositories create adr-repo \
      --repository-format=docker \
      --location=us-central1 \
      --description="Docker repository for ADR service"
    ```

2.  **Configure Docker Authentication:**
    Configure the Docker client to authenticate with Artifact Registry.
    ```bash
    gcloud auth configure-docker us-central1-docker.pkg.dev
    ```

3.  **Tag the Image:**
    Tag your local Docker image with the Artifact Registry path. Replace `<PROJECT_ID>` with your GCP Project ID.
    ```bash
    docker tag adr-service:latest us-central1-docker.pkg.dev/<PROJECT_ID>/adr-repo/adr-service:latest
    ```

4.  **Push the Image:**
    Push the tagged image to the registry.
    ```bash
    docker push us-central1-docker.pkg.dev/<PROJECT_ID>/adr-repo/adr-service:latest
    ```

---

## Step 3: Deploy to Google Cloud Run

Now, deploy the container image from Artifact Registry to Cloud Run.

1.  **Deploy the Service:**
    Run the following command to deploy the service. This command creates a publicly accessible service. For production, you would want to restrict access using `--no-allow-unauthenticated`.
    ```bash
    gcloud run deploy adr-service \
      --image=us-central1-docker.pkg.dev/<PROJECT_ID>/adr-repo/adr-service:latest \
      --platform=managed \
      --region=us-central1 \
      --allow-unauthenticated
    ```

2.  **Verify the Deployment:**
    Once the deployment is complete, `gcloud` will provide a **Service URL**. You can access this URL in your browser or with `curl` to see the welcome message from the service. You can also test the `/adrs` endpoint.

---

## Step 4: Integrate with Google AgentSpace

Integrating your deployed service with Google AgentSpace allows users to interact with it through the AgentSpace interface.

The high-level steps for integration are:
1.  **Discoverability:** In the AgentSpace administrative console, you would add your deployed Cloud Run service as a new **Tool** or **Agent**.
2.  **Configuration:** You will need to provide AgentSpace with the **Service URL** of your deployed `adr-service`.
3.  **API Schema:** You may need to provide an OpenAPI schema (which FastAPI can automatically generate at `/openapi.json`) so that AgentSpace understands how to call your API endpoints (e.g., the `/adrs` endpoint).
4.  **Authentication:** Configure how AgentSpace authenticates with your service. For services on Cloud Run, this is typically managed via IAM service accounts. You would grant the AgentSpace service account the `roles/run.invoker` role on your `adr-service`.

After completing these steps, users in your organization's AgentSpace will be able to invoke your ADR service, for example, by asking a question like, "What are the latest architectural decisions?"