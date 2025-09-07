from fastapi import FastAPI
from pydantic import BaseModel
from src.google_services.docs import create_doc
from src.google_services.slides import create_presentation

app = FastAPI()

class PresentationRequest(BaseModel):
    title: str
    content: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/presentations")
def create_presentation_endpoint(request: PresentationRequest):
    """
    Creates a new Google Doc and Google Slides presentation.
    """
    doc = create_doc(request.title, request.content)
    presentation = create_presentation(request.title, request.content)
    return {
        "document_id": doc.get("documentId"),
        "presentation_id": presentation.get("presentationId"),
    }
