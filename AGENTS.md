# Agent Instructions

## Environment

The recommended way to work on this project is to use the provided development Docker container. This ensures a consistent environment with all necessary dependencies and tools installed.

### Development Workflow

1.  **Build the development image:**
    ```bash
    docker build --target dev -t godot-dev-env .
    ```

2.  **Run the development container:**
    ```bash
    docker run -it --rm -v $(pwd):/app godot-dev-env
    ```

This will place you in a shell inside the container with a pre-configured `uv` virtual environment. All subsequent commands should be run from within this container.
