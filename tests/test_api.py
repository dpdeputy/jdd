import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_create_decision():
    response = client.post(
        "/decisions",
        json={
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
            "more_information": "",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Use FastAPI for the API"
    assert "id" in data


def test_list_decisions():
    response = client.get("/decisions")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_decision():
    # First, create a decision to get
    response = client.post(
        "/decisions",
        json={
            "title": "Another Decision",
            "status": "accepted",
            "date": "2025-09-06",
            "deciders": ["Jules"],
            "consulted": [],
            "informed": [],
            "context_and_problem_statement": "...",
            "decision_drivers": [],
            "considered_options": [],
            "chosen_option": "...",
            "consequences": "...",
            "validation_confirmation": "...",
            "pros_and_cons_of_the_options": "...",
            "more_information": "",
        },
    )
    assert response.status_code == 201
    decision_id = response.json()["id"]

    # Now, get the decision
    response = client.get(f"/decisions/{decision_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == decision_id
    assert data["title"] == "Another Decision"


def test_update_decision():
    # First, create a decision to update
    response = client.post(
        "/decisions",
        json={
            "title": "Decision to be Updated",
            "status": "proposed",
            "date": "2025-09-06",
            "deciders": ["Jules"],
            "consulted": [],
            "informed": [],
            "context_and_problem_statement": "...",
            "decision_drivers": [],
            "considered_options": [],
            "chosen_option": "...",
            "consequences": "...",
            "validation_confirmation": "...",
            "pros_and_cons_of_the_options": "...",
            "more_information": "",
        },
    )
    assert response.status_code == 201
    decision_id = response.json()["id"]

    # Now, update the decision
    response = client.patch(
        f"/decisions/{decision_id}",
        json={"title": "Updated Decision", "status": "accepted"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Decision"
    assert data["status"] == "accepted"
