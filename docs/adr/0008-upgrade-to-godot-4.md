# 8. Upgrade to Godot 4.4.1

*   **Status:** accepted
*   **Date:** 2025-09-06

## Context

The Godot project is currently using Godot 3.x. Godot 4 is a major new version with significant improvements across the board, including a new Vulkan-based renderer, a rewritten GDScript with new features, and numerous performance and usability enhancements. To keep the project modern, benefit from these improvements, and ensure long-term support, an upgrade is necessary.

## Decision

We will upgrade the Godot project from version 3.x to version 4.4.1. The upgrade will be performed using the official project conversion tool provided by Godot 4. This tool helps automate the process of converting project files, scenes, and scripts to be compatible with the new version.

## Consequences

*   **Positive:**
    *   Access to the latest Godot features, including the Vulkan renderer, improved 3D and 2D rendering capabilities, and a more powerful GDScript.
    *   The project will be on a version with long-term support (LTS), ensuring stability and future updates.
    *   Improved performance and a more modern development workflow.
*   **Negative:**
    *   The upgrade process involves breaking changes. All existing scenes and scripts will need to be converted and thoroughly tested.
    *   The unit testing framework (GUT) must be upgraded to a version compatible with Godot 4.
    *   All developers working on the project will need to install Godot 4.4.1.
