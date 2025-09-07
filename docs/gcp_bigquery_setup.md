# GCP BigQuery Setup for dbt

This guide provides step-by-step instructions for setting up a Google Cloud Platform (GCP) project with BigQuery to be used as the data warehouse for this dbt project.

## 1. GCP Project and BigQuery Setup

1.  **Create or Select a GCP Project:**
    *   Navigate to the [GCP Console](https://console.cloud.google.com/).
    *   Create a new project or select an existing one to host your data warehouse.

2.  **Enable the BigQuery API:**
    *   In the GCP Console, go to the "APIs & Services" > "Library".
    *   Search for "BigQuery API" and enable it for your project.

3.  **Create a BigQuery Dataset:**
    *   In the BigQuery section of the GCP Console, create a new dataset. This dataset will be the destination for your dbt models.
    *   Choose a descriptive name for your dataset (e.g., `dbt_jaffle_shop`).
    *   Select the appropriate data location for your dataset.

## 2. IAM Service Account Configuration

1.  **Create a Service Account:**
    *   Go to "IAM & Admin" > "Service Accounts" in the GCP Console.
    *   Click "Create Service Account".
    *   Give the service account a name (e.g., `dbt-runner`) and a description.

2.  **Grant IAM Roles:**
    *   Grant the following IAM roles to the service account. These roles provide the necessary permissions for dbt to interact with BigQuery.
        *   **BigQuery Data Editor:** `roles/bigquery.dataEditor` - Allows dbt to create, delete, and update tables in your dataset. Grant this role on the specific dataset you created.
        *   **BigQuery Job User:** `roles/bigquery.jobUser` - Allows dbt to run jobs (queries, loads, etc.) in your project. Grant this role on the project level.
        *   **BigQuery Read Session User:** `roles/bigquery.readSessionUser` - Allows dbt to read data from BigQuery tables. Grant this role on the project level.
    *   It is recommended to follow the principle of least privilege and only grant the necessary permissions.

## 3. Secure Key and Secrets Management

1.  **Create a JSON Key:**
    *   After creating the service account, go to the "Keys" tab for the service account.
    *   Click "Add Key" > "Create new key".
    *   Select "JSON" as the key type and click "Create". A JSON key file will be downloaded to your computer.

2.  **Securely Manage the Key:**
    *   **IMPORTANT:** Never commit the JSON key file to your git repository.
    *   It is highly recommended to use a secrets manager to store the key securely. Here are some options:
        *   **GCP Secret Manager:** Store the content of the JSON key as a secret in GCP Secret Manager. This is the recommended approach for GCP projects.
        *   **Environment Variables:** For local development, you can set an environment variable with the content of the key file.
        *   **HashiCorp Vault:** If you are using Vault, it's an excellent option for storing the key.

## 4. Update dbt Profile

1.  **Update `profiles.yml`:**
    *   Open the `dbt/jaffle_shop/profiles.yml` file in this project.
    *   Update the file with your BigQuery connection details. Here is a template for using a service account key file:

    ```yaml
    jaffle_shop:
      target: dev
      outputs:
        dev:
          type: bigquery
          method: service-account
          project: [your_gcp_project_id] # Replace with your GCP project id
          dataset: [your_dbt_dataset] # Replace with your dbt dataset
          threads: 1
          keyfile: /path/to/your/service-account-key.json # Replace with the path to your keyfile
    ```

    *   Replace the placeholder values with your actual project ID, dataset name, and the path to your keyfile.

## 5. Execute dbt

1.  **Install Dependencies:**
    *   If you haven't already, install the dbt dependencies using the CLI:
        ```bash
        python src/cli.py deps
        ```

2.  **Run dbt:**
    *   You can now run dbt commands using the CLI. For example, to run all models and tests:
        ```bash
        python src/cli.py build
        ```
