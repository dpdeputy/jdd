# dbt Setup

This document outlines the setup for dbt in this project.

## Overview

We are using dbt for our data transformation layer. It allows us to build, test, and document our data models efficiently.

## Installation

The Python dependencies for dbt, including the `dbt-duckdb` adapter and the Typer CLI, can be installed from the `dbt` optional dependency group:

```bash
uv pip install -e ".[dbt]"
```

Before running any dbt commands, you also need to install the dbt package dependencies using the CLI:
```bash
python src/cli.py deps
```

## dbt Project

The dbt project is located in the `dbt/` directory. The project was initialized using the `jaffle_shop` example. A `profiles.yml` file is included in the project directory to configure the connection to the DuckDB database.

## Typer CLI

A Typer-based CLI has been created in `src/cli.py`. This CLI is the entry point for all dbt-related operations.

You can run dbt commands like this:
```bash
python src/cli.py [COMMAND]
```
For example, to run `dbt build`:
```bash
python src/cli.py build
```

## Testing

dbt provides a robust testing framework to ensure the quality of your data models.

### Types of dbt Tests

1.  **Schema Tests:** These are generic tests defined in your model's `.yml` files. They are used to validate common data assumptions, such as whether a column is unique or not null. The `jaffle_shop` project includes several schema tests.

2.  **Data Tests:** These are custom tests written in SQL. A data test is a SQL query that should return zero rows. If it returns any rows, the test fails. These are useful for testing specific business logic.

### How to Run Tests

To run the tests, you first need to build your dbt models. The `build` command in the CLI will seed the data, run the models, and then execute the tests.

```bash
python src/cli.py build
```

If all tests pass, you can be confident in your data transformations.
