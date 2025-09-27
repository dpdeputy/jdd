# Google Cloud Platform (GCP) Setup Guide

This guide provides instructions for setting up a Google Cloud project and obtaining the necessary credentials to run services that rely on GCP, such as agents using Vertex AI.

---

### Step 1: Set up a Google Cloud Project

Before you can use Google Cloud services, you need a project.

1.  **Go to the Google Cloud Console:** If you don't have a project, you can create one. Visit the [Cloud Resource Manager](https://console.cloud.google.com/cloud-resource-manager) to create a new project or select an existing one.
2.  **Enable Billing:** Ensure that your project has a billing account enabled. Most Google Cloud services, including advanced AI models, require a project with active billing.

---

### Step 2: Enable Necessary APIs

Your application may require specific APIs to be enabled. For example, an AI agent might need the Vertex AI API.

1.  **Navigate to the API Library:** In the Google Cloud Console, go to the "APIs & Services" > "Library" section.
2.  **Search for the API:** Find the API you need (e.g., "Vertex AI API").
3.  **Enable the API:** Click the "Enable" button for that API. This may take a few moments.

---

### Step 3: Install and Authenticate with the gcloud CLI

To allow applications running on your local machine to access Google Cloud services, you need to provide them with credentials. The recommended way to do this for development is by using Application Default Credentials (ADC).

1.  **Install the gcloud CLI:** If you don't have it installed, follow the official instructions to [install the Google Cloud CLI](https://cloud.google.com/sdk/docs/install).
2.  **Authenticate your environment:** Run the following command in your terminal and follow the prompts to log in with your Google account. This command securely stores your credentials on your local machine where Google client libraries can find them.
    ```bash
    gcloud auth application-default login
    ```

---

### Step 4: Obtain an API Key (If Needed)

Some applications can use a simple API key for authentication, although ADC (from the previous step) is often preferred for services like Vertex AI. If you need a standalone API key:

1.  **Navigate to the Credentials Page:** In the Google Cloud Console, go to "APIs & Services" > "Credentials".
2.  **Create a new API Key:** Click "Create Credentials" and select "API key".
3.  **Secure your API Key:** It is critical to restrict your API key to prevent unauthorized use. Add application restrictions (e.g., by IP address) and API restrictions (to limit which APIs the key can call).
4.  **Use the API Key:** Copy the generated API key and use it in your application's configuration, typically in an environment variable or a `.env` file.

By following this guide, you can set up a secure environment for running applications that leverage Google Cloud services.