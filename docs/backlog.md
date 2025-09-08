# Potential Next Steps (Backlog)

This document contains a list of potential next steps that can be taken to further improve the OpenTelemetry implementation in this project. These items are not required for the initial publication but are good candidates for future work.

1.  **Add a Practical Manual Instrumentation Example:** Add a new endpoint to our FastAPI application (`src/app.py`) that includes a custom span with attributes. This would provide a concrete, working example of the manual instrumentation concepts described in the new guide.

2.  **Introduce a Custom Metric:** To demonstrate the metrics capabilities of OpenTelemetry, add a custom counter to the application. For example, we could count how many times a specific business logic function is called. This would show developers how to record business-level metrics.

3.  **Demonstrate a Realistic Local Setup with Jaeger:** To showcase the full power of distributed tracing, add a `docker-compose.yml` file to the project. This would allow a developer to start the application along with an OpenTelemetry Collector and Jaeger (a popular open-source tracing UI) with a single command. This would provide a much richer local development experience for telemetry.
