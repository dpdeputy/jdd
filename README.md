# AI Agent Development on Google Cloud

This repository is a workspace for developing and researching AI agents on the Google Cloud Platform (GCP). It includes experiments, proof-of-concepts, and documentation related to building sophisticated agentic systems.

## Focus Areas

The primary focus of this repository is on leveraging the Google Cloud AI ecosystem, including:

*   **Google Agent Development Kit (ADK):** A code-first framework for building agents.
*   **Vertex AI Agent Engine:** A managed runtime for deploying and scaling agents.
*   **Google AgentSpace:** An enterprise-ready platform for consuming and interacting with AI agents.

## Documentation

This repository contains research and summaries on the Google agent ecosystem. For a detailed overview, please see:

*   **[Research Summary: Google Agent Development on GCP](./docs/gcp_agent_research.md)**
*   **[Presentation: Google Agent Development on GCP](./docs/gcp_agent_presentation.md)**
*   **[Vertex AI Deployment Guide](./docs/vertex_ai_deployment_guide.md)**

## Getting Started

The local development environment uses Python 3.11+ and `uv`.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create a virtual environment:**
    ```bash
    uv venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

4.  **Install dependencies:**
    ```bash
    uv pip install -e ".[test,docs]"
    ```

## Building Documentation

To build the documentation locally, run:
```bash
mkdocs build
```
