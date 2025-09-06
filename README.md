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
