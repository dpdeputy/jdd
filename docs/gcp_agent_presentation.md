---
marp: true
theme: default
---

# **Google Agent Development on GCP**

A summary of the ecosystem for building and deploying custom AI agents on Google Cloud.

---

## The Ecosystem: Three Key Components

1.  **Google Agent Development Kit (ADK)**
    *   The **code-first framework** for building agent logic.
    *   Your primary **development tool**.

2.  **Vertex AI Agent Engine**
    *   The **managed runtime environment** in Vertex AI.
    *   Your **deployment and scaling solution**.

3.  **Google AgentSpace**
    *   The **high-level, user-facing platform**.
    *   Your **consumption and integration layer**.

---

## The Development-to-Deployment Workflow

1.  **Develop** your agent using the **Google ADK**.
2.  **Containerize** your agent application (e.g., with Docker).
3.  **Deploy** the container to the **Vertex AI Agent Engine**.
4.  **Integrate & Expose** the agent in **Google AgentSpace**.
5.  **Interact** with your agent through the AgentSpace UI.

---

## GCP Prerequisites

To get started, you'll need:

*   **APIs Enabled:**
    *   Vertex AI API
    *   Artifact Registry API
*   **Products/Services:**
    *   A license for **Google AgentSpace**.
    *   A GCP project with billing enabled.
*   **IAM Permissions:**
    *   Roles for Vertex AI, Artifact Registry, and AgentSpace.

---

## How to Get Started

1.  **Explore the ADK:** Experiment with the [Google ADK on GitHub](https://github.com/google/adk-python).
2.  **Set up GCP:** Prepare your project with the necessary APIs and permissions.
3.  **Deploy a Sample:** Practice deploying a containerized agent to a GCP service like Cloud Run or GKE.
4.  **Integrate with AgentSpace:** Connect your deployed agent within the AgentSpace administrative interface.

---

## Thank You

Questions?
