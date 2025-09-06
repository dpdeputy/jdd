# Decision Tracker

This is a container-based application for a Decision Tracking framework that uses MADR 3.0. It includes markdown to html site rendering and search capabilities, using Python UV environments and tools.

## Tech Stack

*   Python 3.11
*   FastAPI
*   Markdown
*   uv
*   Docker

## Getting Started

To run this application, you will need Docker installed.

1.  Build the Docker image:
    ```bash
    docker build -t decision-tracker .
    ```

2.  Run the Docker container:
    ```bash
    docker run -p 8000:8000 decision-tracker
    ```

The application will be available at [http://localhost:8000](http://localhost:8000).

## Running with OpenTelemetry

This project is configured to use OpenTelemetry for application telemetry. To run the application with auto-instrumentation and see traces printed to the console, follow these steps. This assumes you have a local Python environment set up.

1.  **Install dependencies:**

    Install the application with its dependencies, including the new OpenTelemetry packages, in an editable mode.
    ```bash
    uv pip install -e .
    ```

2.  **Run the instrumented application:**

    Use the `opentelemetry-instrument` command to run the application with auto-instrumentation. This command will automatically instrument the FastAPI application and export telemetry data to the console.

    ```bash
    opentelemetry-instrument \
        --traces_exporter console \
        --metrics_exporter console \
        --logs_exporter console \
        --service_name decision-tracker \
        uvicorn src.app:app --host 0.0.0.0 --port 8000
    ```

3.  **Generate telemetry:**

    Access the application at [http://localhost:8000](http://localhost:8000) in your browser or with a tool like `curl`. You should see trace information printed to your console.
