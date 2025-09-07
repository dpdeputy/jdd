# Technical Specification: Release 1

## 1. Introduction

This document provides the technical details for the first release of the "Survivalist Strategy Adaptations" game. The focus of this release is to establish the foundational systems, including the main game loop, basic scene setup, and core module initialization. The goal is to create a testable skeleton of the game that can be verified through debug logs.

## 2. System Initialization

The game will be initialized on the server side to ensure authority and security.

*   **Entry Point:** A single `Script` named `Main` will be placed in `ServerScriptService`. This script will be the entry point for all server-side logic.
*   **Module Loading:** The `Main` script will load and initialize the following core modules:
    *   `Log`: A simple logging utility for debug output.
    *   `GameManager`: A singleton module to manage the overall game state.
    *   `TurnManager`: A module to control the flow of the turn-based gameplay.
    *   `ResourceManager`: A module to handle player resources (Energy and Matter).
*   **Initialization Sequence:**
    1.  The `Main` script executes when the server starts.
    2.  The `Log` module is required first to be available for all other modules.
    3.  The `GameManager` is initialized, which in turn initializes the `ResourceManager` and `TurnManager`.
    4.  When a new player joins, the `GameManager` will set up their initial game state (e.g., starting resources).
    5.  The `GameManager` then instructs the `TurnManager` to begin the game loop.

## 3. Main Scene (Workspace Setup)

The main scene will be kept simple for this initial release.

*   **Environment:**
    *   A large, flat `Baseplate` will serve as the ground.
    *   The lighting will be set to a default bright, daytime setting.
*   **Player Representation:**
    *   The player's character will spawn at a designated `SpawnLocation`.
    *   A single `Part` named "Core" will be placed near the spawn point to represent the player's main structure.
*   **Camera:**
    *   The camera will be configured for a top-down or isometric view to give a strategic perspective. A `LocalScript` in `StarterPlayerScripts` will manage this.

## 4. Game Loop Implementation

The game loop is turn-based and managed by the `TurnManager` module.

*   **Turn Structure:** Each turn consists of three phases, executed in order.
    1.  **Player Action Phase:** The server waits for input from the player. For this release, the only player action will be to click a "End Turn" button in the UI. This will fire a `RemoteEvent` to the server.
    2.  **Environment Phase:** This phase is currently a placeholder. The `TurnManager` will call a function that logs a message indicating the phase has run. No actual environmental changes will occur.
    3.  **Resolution Phase:** The consequences of actions are calculated. For instance, any structures that generate resources will have their production added to the player's inventory via the `ResourceManager`.
*   **Flow Control:** The `TurnManager` will manage the transition between phases and turns. The entire loop is server-driven.

## 5. Debug Logging

A simple logging system will be implemented to verify program correctness.

*   **Log Module:** A module named `Log` will provide logging functions:
    *   `Log.info(message)`
    *   `Log.warn(message)`
    *   `Log.error(message)`
*   **Output:** All log messages will be printed to the Roblox Studio Output window, prefixed with the log level and a timestamp (e.g., `[INFO] [13:45:01]: GameManager initialized.`).
*   **Key Log Points:**
    *   Successful initialization of each core module.
    *   Player joining and initial state setup.
    *   The start and end of each turn.
    *   The execution of each phase within a turn.
    *   Any significant event, such as a player action or resource change.

## 6. Code Structure (Initial)

The project will be organized in Roblox Studio as follows:

*   **`ServerScriptService`**
    *   `Main` (Script)
    *   `ServerModules` (Folder)
        *   `GameManager` (ModuleScript)
        *   `TurnManager` (ModuleScript)
        *   `ResourceManager` (ModuleScript)
        *   `Log` (ModuleScript)
*   **`ReplicatedStorage`**
    *   `Events` (Folder)
        *   `EndTurnEvent` (RemoteEvent)
*   **`StarterPlayer`**
    *   `StarterPlayerScripts`
        *   `CameraManager` (LocalScript)
    *   `StarterGui`
        *   `GameUI` (ScreenGui)
            *   `ResourceDisplay` (Frame with TextLabels for Energy and Matter)
            *   `EndTurnButton` (TextButton)
