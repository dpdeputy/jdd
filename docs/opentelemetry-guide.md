# OpenTelemetry Startup and Developer's Guide

Welcome to the OpenTelemetry guide for this project. This document will help you understand how we use OpenTelemetry for application telemetry and how you can effectively contribute.

## 1. Introduction to OpenTelemetry

OpenTelemetry is an open-source observability framework that provides a standardized, vendor-neutral way to collect telemetry data (traces, metrics, and logs) from our applications. By using OpenTelemetry, we can gain deep insights into our application's performance and behavior, which is crucial for debugging, monitoring, and optimization.

## 2. Core Concepts

OpenTelemetry is based on three main types of telemetry data, also known as **signals**:

*   **Traces:** A trace represents the entire journey of a request as it flows through the various services in our system. Each step in the journey is represented by a **span**. Traces are essential for understanding the latency of our application and for pinpointing where errors occur.
*   **Metrics:** Metrics are numerical measurements of our application's performance over time. Examples include the number of requests per second, CPU usage, or memory consumption. Metrics are vital for monitoring the health of our services and for setting up alerts.
*   **Logs:** Logs are timestamped text records of events that occur within our application. They provide detailed context for debugging issues. OpenTelemetry enhances logging by allowing us to correlate logs with traces, so we can see the exact logs that were generated during a specific request.

## 3. Getting Started

This project is set up to use OpenTelemetry auto-instrumentation out of the box. To see it in action, please follow the instructions in the "Running with OpenTelemetry" section of the main `README.md` file. This will show you how to run the application and see traces printed to the console.

## 4. Auto-instrumentation

Our FastAPI application is automatically instrumented using the `opentelemetry-instrumentation-fastapi` library. This means that without any changes to the application code, we automatically get:

*   A new trace for every incoming HTTP request.
*   Spans for the request lifecycle, including routing and response generation.
*   Key attributes on our spans, such as the HTTP method, URL, and status code.

This auto-instrumentation provides a great baseline for our observability, but it doesn't cover everything. For business-specific logic or code that is not part of a standard framework (like our Typer-based tools), we need to use manual instrumentation.

## 5. Manual Instrumentation

Manual instrumentation allows us to add custom spans to our code to get more detailed insights into specific parts of our application.

### Adding a Custom Span

Here is an example of how to add a custom span to a function:

```python
from opentelemetry import trace

# Get a tracer from the global tracer provider
tracer = trace.get_tracer(__name__)

def my_function():
    # Start a new span
    with tracer.start_as_current_span("my_function_span") as span:
        # You can add attributes to the span to provide more context
        span.set_attribute("my.custom.attribute", "my_value")

        # Do some work here
        print("Doing some work in my_function")

        # The span will be automatically finished when the 'with' block is exited
```

To use this in our application, you would first need to get a `tracer` instance. The `opentelemetry-instrument` script ensures that a global tracer provider is configured, so you can get a tracer from anywhere in your code by calling `trace.get_tracer(__name__)`.

## 6. Configuration

OpenTelemetry can be configured using environment variables, which is the recommended approach for our project as it allows us to change the configuration without modifying the code.

Here are some of the key environment variables we use:

*   `OTEL_TRACES_EXPORTER`: Specifies the exporter for traces. Defaults to `otlp`. We use `console` for local development.
*   `OTEL_METRICS_EXPORTER`: Specifies the exporter for metrics. Defaults to `otlp`. We use `console` for local development.
*   `OTEL_LOGS_EXPORTER`: Specifies the exporter for logs. Defaults to `otlp`. We use `console` for local development.
*   `OTEL_SERVICE_NAME`: Specifies the name of the service that is generating the telemetry. This is important for filtering and grouping data in our observability backend.

For example, to send telemetry to an OTLP-compatible backend (like the OpenTelemetry Collector), you would set the exporters to `otlp` and configure the OTLP endpoint:

```bash
export OTEL_TRACES_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4317"
```

## 7. Best Practices

To ensure we get the most out of our telemetry, please follow these best practices:

*   **Span Naming:** Use clear and descriptive names for your spans. A good convention is `<package>.<function>`. For example, `myapp.users.create_user`.
*   **Attributes:** Add meaningful attributes to your spans to provide context. Use the [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/) where possible. For example, use `db.statement` for a database query.
*   **Error Handling:** When an error occurs, record it on the span and set the span's status to `Error`.

    ```python
    from opentelemetry.trace import Status, StatusCode

    try:
        # Some code that might raise an exception
    except Exception as e:
        span.record_exception(e)
        span.set_status(Status(StatusCode.ERROR, "An error occurred"))
        raise
    ```
*   **Performance:** Be mindful of the performance overhead of instrumentation. While OpenTelemetry is designed to be efficient, creating too many spans can have an impact. Use sampling to control the amount of data you collect in production.

By following this guide and these best practices, we can build a highly observable system that is easy to monitor, debug, and maintain.
