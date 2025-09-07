# 9. Use gcloud CLI for GCP Resource Management

*   **Status:** accepted
*   **Date:** 2025-09-07

## Context

The project is intended to be deployed on Google Cloud Platform (GCP) and will interact with various GCP services. We need a consistent and scriptable way to manage these resources, both for local development and for CI/CD pipelines.

## Decision

We will use the `gcloud` command-line interface (CLI) as the primary tool for managing GCP resources. The `gcloud` CLI will be installed in the development and production containers. Developers and CI/CD pipelines will use `gcloud` for tasks such as authenticating with GCP, configuring projects, and deploying services.

## Consequences

*   **Positive:**
    *   Provides a unified and consistent interface for all GCP services.
    *   Enables automation and scripting of GCP management tasks.
    *   Well-documented and officially supported by Google.
*   **Negative:**
    *   Adds an extra dependency to the container image, slightly increasing its size.
    *   Requires developers to learn and be familiar with the `gcloud` CLI commands.
    *   Authentication needs to be managed securely, especially in CI/CD environments.
