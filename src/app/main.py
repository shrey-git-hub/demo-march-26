from fastapi import FastAPI

app = FastAPI(
  title = "Notes App",
  version = "1.0.0",
  description = "lets try building a notes app"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Notes App"}
