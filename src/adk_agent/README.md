# GCS Bucket Listing Agent

This directory contains an AI agent built with the Google Agent Development Kit (ADK). Its purpose is to list the Google Cloud Storage (GCS) buckets in a GCP project.

## How it Works

The agent uses a `tool` that leverages the `google-cloud-storage` Python library to communicate with the GCS API. When prompted, the agent identifies the user's intent and calls this tool to fetch the list of buckets.

## Setup & Authentication

Before running this agent, you must authenticate with Google Cloud.

1.  **Install the Google Cloud CLI:** Follow the official instructions to [install the gcloud CLI](https://cloud.google.com/sdk/docs/install).

2.  **Log in with Application Default Credentials (ADC):** Run the following command and follow the prompts to authenticate. This allows the Python client library to automatically find your credentials.
    ```bash
    gcloud auth application-default login
    ```

3.  **Set your Project:** Ensure your gcloud CLI is configured with the correct project where you want to list buckets.
    ```bash
    gcloud config set project YOUR_PROJECT_ID
    ```
    Replace `YOUR_PROJECT_ID` with your actual GCP project ID.

## How to Run

Once you have authenticated, you can run the agent from the root of the repository:

```bash
python -m src.adk_agent.main
```

The agent will then print its response, which will be the list of GCS buckets found in the configured project.