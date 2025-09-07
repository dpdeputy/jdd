# Project Repository

This repository contains two main projects:
1.  A **Decision Tracker** application built with Python and FastAPI.
2.  A **Godot Project** for experimentation and small feature development.

## Getting Started with Docker (Recommended)

This project is set up to use Docker for a consistent development and production environment. The `Dockerfile` is configured with multi-stage builds to create separate images for development and production.

### Prerequisites

-   **Docker**: You need to have Docker installed on your local machine.

### Development Environment

1.  **Build the development image:**
    ```bash
    docker build --target dev -t godot-dev-env .
    ```

2.  **Run the development container:**
    ```bash
    docker run -it --rm -v $(pwd):/app godot-dev-env
    ```
    This will open a bash shell inside the container with a `uv` virtual environment already set up and all dependencies installed. The current directory is mounted into the container's `/app` directory.

### Production Environment

1.  **Build the production image:**
    ```bash
    docker build -t decision-tracker-prod .
    ```

2.  **Run the production container:**
    ```bash
    docker run -p 8000:8000 decision-tracker-prod
    ```
    The application will be available at [http://localhost:8000](http://localhost:8000).

## Manual Setup (Alternative)

If you prefer not to use Docker, you can set up the environment manually.

### Prerequisites

-   **pyenv**: For managing Python versions.
-   **uv**: For managing Python virtual environments and dependencies.
-   **Godot 3**: The Godot engine (version 3.x) is required to run the Godot project.

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Set up the Python environment:**
    - Create a virtual environment:
      ```bash
      uv venv
      ```
    - Activate the virtual environment:
      ```bash
      source .venv/bin/activate
      ```
    - Install all Python dependencies for both the application and the documentation site:
      ```bash
      uv pip install .[test,docs]
      ```

## Running Tests

### Python Tests
To run the Python unit tests, make sure you are inside the development container or have your manual environment activated, then run:
```bash
pytest
```

### Godot Tests
The Godot project uses the GUT (Godot Unit Test) framework for testing. To run the tests from the development container or your manual setup, use the following command:
```bash
cd godot-project && godot3-server -s addons/gut/gut_cmdln.gd -gdir=res://test/unit -gexit
```
Note: The Godot version will be upgraded to 4.4.1 in the new Docker environment. The command to run tests might change after the upgrade.
