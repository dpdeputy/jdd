# Documentation Suggestions

This document outlines suggestions for additional documentation coverage to improve the developer experience and maintainability of the project.

## 1. Detailed CLI Guide

We should create a more detailed guide on how to use the Typer-based CLI for dbt commands. This guide should include:
*   An overview of all available commands (`build`, `test`, `run`, `seed`, `deps`, `parse`).
*   Examples for each command, showing the expected output.
*   Instructions on how to add new commands to the CLI.

## 2. dbt Development Guide

A guide on how to develop with dbt in this project would be very helpful. It should cover:
*   How to add new dbt models.
*   How to write and run schema and data tests.
*   Best practices for organizing dbt models and tests.
*   A style guide for writing dbt SQL.

## 3. Jaffle Shop Project Overview

The `jaffle_shop` dbt project is a great example, but it would be beneficial to have a document that explains its data models and their relationships. This would help new developers understand the project structure and how the different models are connected.

## 4. BigQuery Credentials Management

We should create a guide on how to manage BigQuery credentials securely. This guide should include:
*   Instructions on how to create a service account with the necessary permissions in GCP.
*   Best practices for storing and using the service account keyfile securely.
*   (This section can be a placeholder until the final credentials strategy is decided).

## 5. Previewing Documentation Locally

We should add a section to the `README.md` or the main `index.md` that explains how to run the `mkdocs` site locally to preview the documentation. This would involve a command like `mkdocs serve`.
