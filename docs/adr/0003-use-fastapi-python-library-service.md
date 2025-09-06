# 3. Use FastAPI for the API Service

*   **Status:** accepted
*   **Date:** 2025-09-05

## Context

The project requires a RESTful API to provide programmatic access to the ADRs. The API needs to be fast, modern, and have automatic, interactive documentation, as stated in the requirements.

## Decision

We will use FastAPI, a modern, high-performance Python web framework for building APIs. FastAPI is built on Starlette and Pydantic, and it provides automatic generation of interactive API documentation (using Swagger UI and ReDoc). Its use of Python type hints for data validation and serialization simplifies development and reduces errors.

## Consequences

*   **Positive:**
    *   High performance, on par with NodeJS and Go.
    *   Automatic generation of interactive API documentation, which fulfills a key requirement.
    *   Type-hint based data validation is robust and developer-friendly.
    *   FastAPI has a growing community and excellent documentation.
*   **Negative:**
    *   The decision to use FastAPI over the initially implemented Flask means we need to replace the existing `app.py`. This is a small change at this early stage.
    *   FastAPI is newer than Flask or Django, so there are fewer experienced developers. However, its excellent documentation mitigates this.
