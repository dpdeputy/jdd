# 6. Use SQLModel for the Data Model

*   **Status:** proposed
*   **Date:** 2025-09-05

## Context

The application needs to interact with a database (as decided in ADR-0004, DuckDB) and handle data validation for the API. We need a way to define our data models that can be used for both database interaction (creating tables, querying data) and API validation (parsing request bodies, serializing responses). Using separate libraries for the ORM (like SQLAlchemy) and data validation (like Pydantic) can lead to code duplication and inconsistencies.

## Decision

We will use `SQLModel`, a library that combines Pydantic and SQLAlchemy. It is designed to be a single source of truth for our data models. With SQLModel, we can define our models once and use them as both Pydantic models for FastAPI validation and SQLAlchemy models for database operations. This simplifies the codebase and reduces the chance of a mismatch between the API layer and the database layer.

## Consequences

*   **Positive:**
    *   Reduces code duplication by defining data models only once.
    *   Ensures consistency between database models and API models.
    *   Excellent integration with FastAPI, as they are created by the same author.
    *   Provides the power of both Pydantic (for data validation) and SQLAlchemy (for database interaction).
    *   Still compatible with DuckDB, as DuckDB has a SQLAlchemy dialect.
*   **Negative:**
    *   SQLModel is a relatively new library, so the community and ecosystem are smaller than for SQLAlchemy or Pydantic alone.
    *   Adds another layer of abstraction, which might have a slight learning curve for developers unfamiliar with it.
