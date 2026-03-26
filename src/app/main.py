from fastapi import FastAPI

app = FastAPI(
  title = "Notes API",
  version = "1.0.0",
  description = "A simple API for creating, reading, updating, and deleting notes."
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Notes App"}

@app.on_event("startup")
async def startup_event():
    print("INFO:     Application startup complete.")

@app.on_event("shutdown")
async def shutdown_event():
    print("INFO:     Application shutdown complete.")