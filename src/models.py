from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Decision(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    status: str
    date: str
    deciders: List[str]
    consulted: List[str]
    informed: List[str]
    context_and_problem_statement: str
    decision_drivers: List[str]
    considered_options: List[str]
    chosen_option: str
    consequences: str
    validation_confirmation: str
    pros_and_cons_of_the_options: str
    more_information: str


class DecisionUpdate(BaseModel):
    title: Optional[str] = None
    status: Optional[str] = None
    date: Optional[str] = None
    deciders: Optional[List[str]] = None
    consulted: Optional[List[str]] = None
    informed: Optional[List[str]] = None
    context_and_problem_statement: Optional[str] = None
    decision_drivers: Optional[List[str]] = None
    considered_options: Optional[List[str]] = None
    chosen_option: Optional[str] = None
    consequences: Optional[str] = None
    validation_confirmation: Optional[str] = None
    pros_and_cons_of_the_options: Optional[str] = None
    more_information: Optional[str] = None
