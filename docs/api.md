# API Design

This document outlines the API design for the Decision Tracking application.

## 1. Data Model

The API uses a data model based on the [MADR 3.0.0 specification](https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html).

A decision record (ADR) has the following fields:

- **id**: A unique identifier for the decision (string, server-generated).
- **title**: The title of the decision (string, required).
- **status**: The status of the decision (string, e.g., "proposed", "accepted", "rejected", "deprecated", "superseded by").
- **date**: The date the decision was last updated (string, "YYYY-MM-DD" format).
- **deciders**: A list of people involved in the decision (list of strings).
- **consulted**: A list of people whose opinions were sought (list of strings).
- **informed**: A list of people who were kept up-to-date (list of strings).
- **context_and_problem_statement**: The context and problem statement (string, Markdown).
- **decision_drivers**: The decision drivers (list of strings).
- **considered_options**: The considered options (list of strings).
- **chosen_option**: The chosen option (string).
- **consequences**: The consequences of the decision (string, Markdown).
- **validation_confirmation**: How the implementation of the ADR is evaluated (string, Markdown).
- **pros_and_cons_of_the_options**: The pros and cons of the options (string, Markdown).
- **more_information**: Additional information (string, Markdown).

## 2. API Endpoints

### 2.1. Create a new proposed decision

- **Method:** `POST`
- **Endpoint:** `/decisions`
- **Request Body:** A JSON object representing the new decision.
- **Response:**
  - **Success (201 Created):** The newly created decision object, including a server-generated ID.
  - **Failure (400 Bad Request):** An error message if the request body is invalid.

**Example Request:**

```json
{
  "title": "Use FastAPI for the API",
  "status": "proposed",
  "date": "2025-09-06",
  "deciders": ["Jules"],
  "consulted": [],
  "informed": [],
  "context_and_problem_statement": "We need to choose a web framework for the API.",
  "decision_drivers": ["Performance", "Ease of use"],
  "considered_options": ["FastAPI", "Flask", "Django"],
  "chosen_option": "FastAPI",
  "consequences": "We will use FastAPI for the API.",
  "validation_confirmation": "The API will be implemented using FastAPI.",
  "pros_and_cons_of_the_options": "FastAPI is fast and easy to use.",
  "more_information": ""
}
```

### 2.2. List all decisions

- **Method:** `GET`
- **Endpoint:** `/decisions`
- **Query Parameters:**
  - `status`: Filter by status.
  - `decider`: Filter by decider.
  - `consulted`: Filter by consulted.
  - `informed`: Filter by informed.
- **Response:**
  - **Success (200 OK):** An array of decision objects.

### 2.3. Get a single decision

- **Method:** `GET`
- **Endpoint:** `/decisions/{decision_id}`
- **Response:**
  - **Success (200 OK):** The decision object with the specified ID.
  - **Failure (404 Not Found):** If no decision with that ID exists.

### 2.4. Edit a decision

- **Method:** `PATCH`
- **Endpoint:** `/decisions/{decision_id}`
- **Request Body:** A JSON object containing the fields to be updated.
- **Response:**
  - **Success (200 OK):** The updated decision object.
  - **Failure (400 Bad Request):** If the request body is invalid.
  - **Failure (404 Not Found):** If no decision with that ID exists.
```
