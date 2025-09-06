# 7. Add Godot Project for Experimentation

*   **Status:** accepted
*   **Date:** 2025-09-06

## Context

The project requires a basic local environment for Godot experimentation and small feature development. The goal is to support parallel feature development pipelines and establish the necessary tools and processes for a Godot development workflow within this repository.

## Decision

We will add a Godot project to this repository. The project will be located in a subdirectory named `godot-project/` to keep it separate from the existing Python application. This approach allows both projects to coexist in the same repository while maintaining a clear separation of concerns. The Godot project will be initialized with a basic "Hello, World!" scene and will include a unit testing setup using the GUT (Godot Unit Test) framework.

## Consequences

*   **Positive:**
    *   Provides a dedicated and version-controlled environment for Godot development and experimentation.
    *   Co-locating the Godot project with the Python application allows for potential future integration and simplifies repository management.
    *   The inclusion of the GUT testing framework from the start promotes a test-driven development culture for the Godot project.
*   **Negative:**
    *   Increases the complexity of the repository, as it now contains two distinct projects with different technology stacks.
    *   Requires developers to have both Python and Godot development environments set up on their local machines.
    *   The CI/CD pipeline (if any) will need to be configured to handle both Python and Godot projects.
