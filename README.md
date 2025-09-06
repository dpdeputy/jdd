# Project Repository

This repository contains two main projects:
1.  A **Decision Tracker** application built with Python and FastAPI.
2.  A **Godot Project** for experimentation and small feature development.

## Getting Started

This project uses `pyenv` to manage Python versions and `uv` to manage Python dependencies. It is recommended to work inside a virtual environment.

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

## Python Decision Tracker

This is a web application for a Decision Tracking framework that uses MADR 3.0. It includes markdown to html site rendering and search capabilities.

### Running the application
(Instructions to be added once the application is more developed)

### Running the tests
To run the Python unit tests, make sure your virtual environment is activated and run:
```bash
pytest
```

## Godot Project

This is a basic Godot project for experimentation and small feature development.

### Running the project
(Instructions to be added)

### Running the tests
The Godot project uses the GUT (Godot Unit Test) framework for testing. To run the tests, use the following command from the root of the repository:
```bash
cd godot-project && godot3-server -s addons/gut/gut_cmdln.gd -gdir=res://test/unit -gexit
```
