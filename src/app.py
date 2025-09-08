from typing import List
from uuid import UUID

from fastapi import FastAPI, HTTPException

from src.models import Decision, DecisionUpdate

app = FastAPI()

# In-memory database
db: List[Decision] = []


@app.post("/decisions", response_model=Decision, status_code=201)
def create_decision(decision: Decision):
    db.append(decision)
    return decision


@app.get("/decisions", response_model=List[Decision])
def list_decisions(
    status: str = None,
    decider: str = None,
    consulted: str = None,
    informed: str = None,
):
    results = db
    if status:
        results = [d for d in results if d.status == status]
    if decider:
        results = [d for d in results if decider in d.deciders]
    if consulted:
        results = [d for d in results if consulted in d.consulted]
    if informed:
        results = [d for d in results if informed in d.informed]
    return results


@app.get("/decisions/{decision_id}", response_model=Decision)
def get_decision(decision_id: UUID):
    for decision in db:
        if decision.id == decision_id:
            return decision
    raise HTTPException(status_code=404, detail="Decision not found")


@app.patch("/decisions/{decision_id}", response_model=Decision)
def update_decision(decision_id: UUID, decision_update: DecisionUpdate):
    for i, decision in enumerate(db):
        if decision.id == decision_id:
            updated_decision = decision.model_copy(
                update=decision_update.model_dump(exclude_unset=True)
            )
            db[i] = updated_decision
            return updated_decision
    raise HTTPException(status_code=404, detail="Decision not found")
