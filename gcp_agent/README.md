# GCP Agent

This agent provides a simple interface to manage Google Cloud Platform (GCP) resources using the `gcloud` command-line tool.

## Setup

1.  **Install the Google Cloud SDK:**
    Follow the official instructions to install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) on your local machine.

2.  **Authenticate with GCP:**
    Before using the agent, you need to authenticate with your GCP account. Run the following command and follow the prompts:
    ```bash
    gcloud auth login
    ```

3.  **Set your project:**
    Configure the agent to use your desired GCP project:
    ```bash
    gcloud config set project YOUR_PROJECT_ID
    ```
    Replace `YOUR_PROJECT_ID` with your actual GCP project ID.

## Usage

You can use the agent to perform various tasks, such as listing your GCP projects, managing virtual machines, and interacting with other GCP services.

To run the agent, execute the `main.py` script:
```bash
python gcp_agent/main.py
```
