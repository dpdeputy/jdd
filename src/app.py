from fastapi import FastAPI
from fastmcp.server.server import FastMCP

app = FastAPI(
    title="Decision Tracker",
    description="A container-based application for a Decision Tracking framework using MADR 3.0",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

server = FastMCP.from_fastapi(
    app,
    name="decision-tracker",
    instructions="This is the Decision Tracker. It can be used to track decisions.",
)

if __name__ == "__main__":
    server.run()
