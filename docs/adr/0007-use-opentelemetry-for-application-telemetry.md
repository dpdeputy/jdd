# 7. Use OpenTelemetry for Application Telemetry

*   **Status:** accepted
*   **Date:** 2025-09-06

## Context

The project requires a standardized way to collect telemetry data (metrics, traces, and logs) from its Python-based applications and services, including the FastAPI service and any Typer-based command-line tools. This is crucial for monitoring application performance, diagnosing issues, and gaining insights into application behavior, especially in a containerized environment. The chosen solution should be vendor-neutral, widely adopted, and support auto-instrumentation to minimize boilerplate code.

## Decision

We will adopt OpenTelemetry as the standard for instrumenting our Python applications for telemetry. OpenTelemetry is an open-source observability framework that provides a unified set of APIs, libraries, agents, and collector services to capture distributed traces and metrics from our applications.

For a detailed guide on how to use OpenTelemetry in this project, please see the [OpenTelemetry Startup and Developer's Guide](../opentelemetry-guide.md).

## Consequences

*   **Positive:**
    *   **Standardization:** Provides a single, consistent way to handle telemetry across all our Python services.
    *   **Vendor-Neutrality:** Avoids vendor lock-in for our observability backend. We can switch backends by changing the OpenTelemetry Collector configuration without changing the application code.
    *   **Auto-instrumentation:** Reduces the amount of manual instrumentation code we need to write, especially for common frameworks like FastAPI.
    *   **Rich Ecosystem:** OpenTelemetry is a CNCF project with a large and active community, ensuring good support and a wide range of integrations.
    *   **Correlated Signals:** Enables correlation of traces, metrics, and logs, providing a holistic view of our applications.

*   **Negative:**
    *   **Learning Curve:** The team will need to familiarize themselves with OpenTelemetry concepts and APIs.
    *   **Overhead:** There is a slight performance overhead associated with collecting and exporting telemetry data.
    *   **Configuration:** Setting up and managing the OpenTelemetry Collector for production environments requires some effort.
