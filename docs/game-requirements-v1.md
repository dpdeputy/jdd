# Game Requirements: Survivalist Strategy Adaptations (v1)

## 1. Overview

This document outlines the initial requirements for a turn-based survival strategy game inspired by titles like Factorio and Cell to Singularity. The game will focus on resource gathering, technology progression, and adaptation to environmental challenges. The first version will establish the core mechanics in a simplified form.

## 2. Core Gameplay Loop

The game will be turn-based. Each turn, the player can perform a set of actions. The core loop is as follows:

1.  **Player Action Phase:** The player spends action points to perform tasks such as gathering resources, building structures, or researching technology.
2.  **Environment Phase:** The environment updates based on a set of predefined rules (e.g., resources deplete, new challenges emerge).
3.  **Resolution Phase:** The consequences of the player's actions and environmental changes are calculated and applied.

## 3. Key Features (Release 1)

### 3.1. Resource Management

*   **Basic Resources:** The game will start with two primary resources: "Energy" and "Matter."
*   **Gathering:** Players can gather resources from the environment. Initially, this will be a simple action that yields a fixed amount of resources per turn.
*   **Storage:** Resources are stored in a central inventory with a defined capacity.

### 3.2. Technology Tree

*   **Simple Progression:** A linear technology tree will be implemented.
*   **Unlocking Abilities:** Researching technologies will unlock new abilities, such as improved resource gathering or new building options.
*   **Example Techs:**
    *   **Tier 1:** Basic Tools (improves Matter gathering).
    *   **Tier 2:** Energy Condensers (improves Energy gathering).

### 3.3. Building and Structures

*   **Initial Structure:** The player starts with a single "Core" structure.
*   **Building:** Players can build new structures on a grid-based map.
*   **Example Structures:**
    *   **Collector:** Automatically gathers Matter each turn.
    *   **Generator:** Automatically generates Energy each turn.

### 3.4. Game State

*   **Win Condition:** The game is won by reaching the final technology in the tech tree.
*   **Lose Condition:** The game is lost if the player's Core is destroyed or if they run out of resources and cannot perform any actions.

## 4. User Interface (UI)

*   **Resource Display:** A clear display of the player's current Energy and Matter.
*   **Action Bar:** A simple UI for selecting actions (gather, build, research).
*   **Tech Tree View:** A screen to view the technology tree and select research goals.
*   **Game Log:** A text log that displays events from the current turn.

## 5. Technical Requirements

*   **Platform:** Roblox
*   **Language:** Luau
*   **Persistence:** The game state should be saved between sessions (future requirement, not for release 1).
*   **Modularity:** The code should be organized into modules for resource management, technology, and UI.
