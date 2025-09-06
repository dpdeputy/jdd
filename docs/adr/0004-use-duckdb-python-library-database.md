# 4. Use DuckDB for the Database

*   **Status:** accepted
*   **Date:** 2025-09-05

## Context

The application needs a database to store and search the ADRs. The search functionality needs to be efficient. The database should be simple to manage, embeddable within the application, and have good performance for analytical queries (like searching through text).

## Decision

We will use DuckDB as the database for this application. DuckDB is an in-process SQL OLAP database management system. It's file-based, requires no external dependencies (it can be installed via pip), and is extremely fast for analytical queries. We can store the ADRs in a DuckDB file and leverage its full-text search capabilities for the search feature.

## Consequences

*   **Positive:**
    *   No need for a separate database server, simplifying deployment and development.
    *   Excellent performance for the kind of text-based search queries we will need.
    *   Simple to use with a Pythonic API.
    *   The database is a single file that can be easily backed up or version-controlled (though we should be careful with the latter).
*   **Negative:**
    *   DuckDB is not designed for high-concurrency transactional workloads (OLTP), but this is not a requirement for our application.
    *   Being a newer database, it has a smaller community compared to SQLite or PostgreSQL.
