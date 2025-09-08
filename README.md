# Decision Tracker

This is a container-based application for a Decision Tracking framework that uses MADR 3.0. It includes markdown to html site rendering and search capabilities, using Python UV environments and tools.

## Tech Stack

*   Python 3.11
*   FastAPI
*   Markdown
*   uv
*   Docker

## API

The application exposes a RESTful API for managing decision records. For more details, see the [API Documentation](docs/api.md).

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

## Local Development

For local development, you will need Python 3.11+ and `uv` installed.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/example/decision-tracker.git
    cd decision-tracker
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
    To install all dependencies, including for testing and documentation, run:
    ```bash
    uv pip install -e ".[test,docs]"
    ```

5.  **Run the application:**
    ```bash
    uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
    ```

6.  **Run tests:**
    ```bash
    pytest
    ```

7.  **Build documentation:**
    ```bash
    mkdocs build
    ```
