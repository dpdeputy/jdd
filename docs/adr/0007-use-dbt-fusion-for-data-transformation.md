# 7. Use dbt Fusion for Data Transformation

*   **Status:** proposed
*   **Date:** 2025-09-06

## Context

The project requires a robust and efficient data transformation solution. As we anticipate dealing with complex data models and a growing volume of data, performance and developer productivity are key considerations. We need a tool that can handle modern data engineering challenges, integrates well with our existing Python-based stack, and has a strong community and support system.

## Decision

We will adopt dbt Fusion as our primary tool for data transformation. dbt Fusion, with its Rust-based engine, offers significant performance improvements over traditional dbt Core. It will be used to build, test, and document our data transformation pipelines. We will use the `dbt-duckdb` adapter to integrate with our DuckDB database. A Typer-based CLI will be developed to streamline the execution of dbt commands within our project.

## Consequences

*   **Positive:**
    *   **Performance:** dbt Fusion's Rust-based engine will significantly speed up our data transformation jobs.
    *   **Developer Experience:** dbt Fusion provides a modern and efficient development workflow, especially when combined with the official VS Code extension.
    *   **Scalability:** dbt is designed for complex data projects and will scale with our needs.
    *   **Integration:** The `dbt-duckdb` adapter allows for seamless integration with our existing DuckDB data warehouse.
    *   **Standardization:** Adopting dbt brings a widely-recognized standard for data transformation to our project.

*   **Negative:**
    *   **New Dependency:** We are introducing a new tool into our stack that needs to be installed and managed. dbt Fusion is installed via a shell script, which is a departure from our Python-based dependency management.
    *   **Learning Curve:** The team will need to learn the dbt way of working, including its project structure, Jinja templating, and best practices.
    *   **CLI Overhead:** Building and maintaining a custom Typer CLI for dbt commands adds a layer of abstraction and requires development effort.
