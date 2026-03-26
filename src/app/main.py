from fastapi import FastAPI

app = FastAPI(
  title = "Notes API",
  version = "1.0.0",
  description = "A simple API for creating, reading, updating, and deleting notes."
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Notes App"}
