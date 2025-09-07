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

## Presentation Generation

This application can generate Google Docs and Slides presentations. To use this feature, you need to enable the Google Docs and Google Slides APIs and create OAuth 2.0 credentials.

1.  **Enable the APIs:**
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or select an existing one.
    - In the navigation menu, go to **APIs & Services > Library**.
    - Search for and enable the **Google Docs API** and the **Google Slides API**.

2.  **Create OAuth 2.0 Credentials:**
    - In the navigation menu, go to **APIs & Services > Credentials**.
    - Click **Create Credentials > OAuth client ID**.
    - Select **Desktop app** as the application type.
    - Give your client ID a name and click **Create**.
    - Download the JSON file and save it as `credentials.json` in the root of this project.

3.  **Generate a Presentation:**
    - Make a POST request to the `/presentations` endpoint with a title and content in the request body.
    - The first time you run this, you will be prompted to authorize the application in your browser.

    ```bash
    curl -X POST "http://localhost:8000/presentations" \
    -H "Content-Type: application/json" \
    -d '{
        "title": "My Awesome Presentation",
        "content": "This is the content of my presentation."
    }'
    ```
