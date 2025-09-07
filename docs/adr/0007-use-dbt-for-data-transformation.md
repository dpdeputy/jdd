# 7. Use dbt for Data Transformation

*   **Status:** accepted
*   **Date:** 2025-09-07
*   **Supersedes:** ADR-0004: Use DuckDB as the database

## Context

The project requires a robust and efficient data transformation solution. As we anticipate dealing with complex data models and a growing volume of data, performance and developer productivity are key considerations. We need a tool that can handle modern data engineering challenges, integrates well with our existing Python-based stack, and has a strong community and support system.

Our initial exploration was to use dbt Fusion with DuckDB. However, we discovered that the `dbt-duckdb` Python adapter is not compatible with the dbt Fusion engine, which requires a native ADBC adapter. This led us to re-evaluate our choice of data warehouse.

## Decision

We will use dbt for our data transformation pipelines, with Google BigQuery as our data warehouse. This decision is documented in ADR-0008.

dbt will be used to build, test, and document our data transformation pipelines. A Typer-based CLI will be developed to streamline the execution of dbt commands within our project.

## Consequences

*   **Positive:**
    *   **Performance and Scalability:** By using dbt with BigQuery, we can leverage a highly scalable and performant data warehouse. This setup is also compatible with the dbt Fusion engine, which we can explore in the future.
    *   **Developer Experience:** dbt provides a modern and efficient development workflow for data transformation.
    *   **Standardization:** Adopting dbt brings a widely-recognized standard for data transformation to our project.

*   **Negative:**
    *   **Complexity:** The setup with BigQuery is more complex than with an embedded database like DuckDB.
    *   **Learning Curve:** The team will need to learn the dbt way of working, including its project structure, Jinja templating, and best practices.
    *   **CLI Overhead:** Building and maintaining a custom Typer CLI for dbt commands adds a layer of abstraction and requires development effort.
