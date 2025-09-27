import os
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="ADR Service",
    description="An API for accessing Architectural Decision Records (ADRs).",
    version="0.1.0",
)

# In a real containerized environment, the path should be absolute.
# For this example, we assume the app runs from the repository root.
ADR_DIRECTORY = "docs/adr"


@app.get("/")
def read_root():
    """A simple endpoint to confirm the service is running."""
    return {"message": "Welcome to the ADR Service!"}


@app.get("/adrs")
def list_adrs():
    """
    Retrieves a list of available Architectural Decision Records (ADRs).
    """
    try:
        if not os.path.isdir(ADR_DIRECTORY):
            raise HTTPException(status_code=404, detail="ADR directory not found.")

        files = os.listdir(ADR_DIRECTORY)
        adr_files = sorted([f for f in files if f.endswith(".md")])
        return {"adrs": adr_files}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
