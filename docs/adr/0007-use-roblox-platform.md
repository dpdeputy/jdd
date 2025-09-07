# 7. Use Roblox Platform for Game Development Experimentation

*   **Status:** proposed
*   **Date:** 2025-09-07

## Context

We want to experiment with game development workflows and create a simple turn-based survival strategy game. We need a platform that allows for rapid prototyping, has a low barrier to entry, and provides a clear path to multiplayer and cross-platform deployment. The goal is to learn and iterate quickly on game mechanics without getting bogged down in complex engine development or infrastructure setup.

## Decision

We will use the Roblox platform for our initial game development experiments. Roblox provides a free, all-in-one solution that includes the Roblox Studio (a game editor and IDE), cloud hosting, and a massive user base. The scripting language is Luau, which is a sandboxed and gradually typed version of Lua, making it relatively easy to learn.

## Consequences

*   **Positive:**
    *   **Rapid Prototyping:** Roblox Studio and the integrated asset marketplace will allow us to build and test ideas quickly.
    *   **Low Cost:** The platform is free to use for development and deployment.
    *   **Built-in Multiplayer:** Roblox's infrastructure is designed for multiplayer games, simplifying the process of creating shared experiences.
    *   **Cross-Platform:** Games created on Roblox are automatically available on PC, Mac, mobile devices, and Xbox.
    *   **Large Community:** There is a vast amount of documentation, tutorials, and community support available.

*   **Negative:**
    *   **Platform Lock-in:** The game will be tied to the Roblox ecosystem and its terms of service.
    *   **Technical Constraints:** We will be limited by the capabilities and performance of the Roblox engine.
    *   **Monetization:** While not an initial focus, monetization is heavily controlled by Roblox's systems (e.g., Robux).
    *   **Perception:** Roblox is often associated with games for younger audiences, which might not align with future project goals.
