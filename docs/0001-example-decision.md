# 1. Example Decision

*   **Status:** proposed
*   **Date:** 2025-09-05
*   **Deciders:** Jules
*   **Consulted:**
*   **Informed:**

## Context and Problem Statement

When starting a new project, it's important to have a clear and well-defined structure. This helps with maintainability, scalability, and onboarding new developers. The problem is to decide on an initial project structure for this decision tracking application.

## Decision Drivers

*   Need for a clear separation of concerns (e.g., source code, documentation, containerization).
*   Ease of use for developers.
*   Compatibility with standard Python tooling.
*   Support for containerization with Docker.

## Considered Options

1.  **Flat structure:** All files in the root directory.
2.  **Simple structure with `src` and `docs`:** A `src` directory for source code and a `docs` directory for documentation.
3.  **More complex structure with additional directories:** e.g., for tests, scripts, etc.

## Decision Outcome

Chosen option: "Simple structure with `src` and `docs`", because it provides a good balance between simplicity and organization for a project of this size. It's a common and well-understood structure in the Python community.

### Positive Consequences

*   The project is well-organized from the start.
*   It's easy to find source code and documentation.
*   The structure can be easily extended as the project grows.

### Negative Consequences

*   Slightly more complex than a flat structure, which might be overkill for a very small project.

## Pros and Cons of the Options

### Flat structure

*   Good, because it's very simple.
*   Bad, because it can become messy as the project grows.

### Simple structure with `src` and `docs`

*   Good, because it provides a clear separation of concerns.
*   Good, because it's a common and well-understood structure.
*   Bad, because it might be slightly more complex than necessary for a tiny project.

### More complex structure

*   Good, because it's very organized and scalable.
*   Bad, because it's overkill for a small project and can add unnecessary complexity.

## Links

*   [MADR project](https://github.com/adr/madr)
