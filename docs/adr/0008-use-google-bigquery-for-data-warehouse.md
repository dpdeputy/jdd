# 8. Use Google BigQuery for Data Warehouse

*   **Status:** accepted
*   **Date:** 2025-09-07

## Context

The project requires a data warehouse that is scalable, performant, and well-integrated with our data transformation tools. Our initial choice of DuckDB, while excellent for local development, presented challenges with the dbt Fusion engine due to the lack of a compatible ADBC adapter. To fully leverage the performance benefits of dbt Fusion, we need a data warehouse with official support.

## Decision

We will use Google BigQuery as our primary data warehouse. BigQuery is a serverless, highly scalable, and cost-effective data warehouse that is officially supported by dbt Fusion with a native ADBC adapter. This will allow us to take full advantage of dbt Fusion's performance improvements for parsing and compiling our dbt projects.

We will use the `dbt-bigquery` adapter to connect to BigQuery. The authentication will be handled via IAM service accounts, with the credentials to be provided through a secure credentials management strategy.

## Consequences

*   **Positive:**
    *   **dbt Fusion Compatibility:** BigQuery has first-class support in dbt Fusion, enabling us to use the high-performance Rust-based engine.
    *   **Scalability:** BigQuery's serverless architecture allows it to handle massive datasets and complex queries without the need to manage infrastructure.
    *   **Performance:** BigQuery is known for its high query performance, which will be beneficial as our data grows.
    *   **Ecosystem Integration:** BigQuery is deeply integrated with the Google Cloud Platform (GCP) ecosystem, which can be leveraged for other data-related tasks.
    *   **Managed Service:** As a fully managed service, BigQuery reduces operational overhead.

*   **Negative:**
    *   **Vendor Lock-in:** By choosing BigQuery, we are tying a part of our data infrastructure to Google Cloud Platform.
    *   **Cost:** While cost-effective, BigQuery's pricing is based on data storage and query usage, which will need to be monitored to manage costs.
    *   **Complexity:** Setting up the IAM permissions and managing the BigQuery environment can be more complex than a simple file-based database like DuckDB.
    *   **Local Development:** Local development will require a connection to BigQuery, which might be less convenient than using an embedded database like DuckDB.
